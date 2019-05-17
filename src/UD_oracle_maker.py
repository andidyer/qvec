import json
import re
import time
import sys
import argparse
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument("in_conll")
parser.add_argument("out_file")
parser.add_argument("--tag_type", default='upos', help='ud tag to use.  upos or deprel')
parser.add_argument("--freq_filter", type=int, default=0, help='frequency filter for word appearance')
parser.add_argument("--topN", type=int, default=None, help='retain only topN most frequent words')
parser.add_argument("--verbose", action='store_true')
args = parser.parse_args()


conllfile = args.in_conll

tab = re.compile('^(?:[^\t]+\t){9}[^\t]+$')
fine_deprel = re.compile(':\w+$')

freqfilter=args.freq_filter
topN = args.topN

if args.verbose:
    print('reading from', conllfile)

rus=open(conllfile)
#Step 1: Get frequency and tag distributions of words
words = {}
for line in rus:
    line = line.strip()
    if tab.match(line):
        index, form, lemma, UPOS, CPOS, feats, head, deprel, deps, misc = line.split('\t')
        form = form.lower()
        try:
            words[form]['freq'] += 1
        except:
            words[form] = {'freq':1, 'tags':defaultdict(float)}
        if args.tag_type == 'upos':
            tag = UPOS
        elif args.tag_type == 'deprel':
            tag = fine_deprel.sub('', deprel)
        else:
            raise Exception('require either upos or deprel as tag_type')
        words[form]['tags']['ud.'+tag.lower()] += 1
rus.close()

if args.verbose:
    print('read all words from file')

#Step 2: Filter by frequency (optional)
words = {k:v for k,v in words.items() if words[k]['freq'] >= freqfilter}

#Step 3: Keep only top N (optional)
if topN:
    words = {k: words[k] for k in sorted(words, key=lambda x: words[x]['freq'], reverse=True)[:topN]}

#Step 4: Convert counts to probability distribution
for w in words:
    tagsum = sum(words[w]['tags'].values())
    for t in words[w]['tags']:
        words[w]['tags'][t] = words[w]['tags'][t] / tagsum

#Step 5: Print to file
with open(args.out_file,'w') as output:
    for w in sorted(words):
        print(w, json.dumps(words[w]['tags']), sep='\t', file =output)

if args.verbose:
    print('finished {}'.format(time.ctime()))
    
