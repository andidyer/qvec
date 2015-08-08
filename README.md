QVEC
========

Intrincsic evaluation of word vectors representations by subspace alignment.

<a href="http://www.cs.cmu.edu/~ytsvetko/papers/qvec.pdf">Evaluation of Word Vector Representations by Subspace Alignment</a>
  </li> 

### Usage
#### Semantic content evaluation: 

```py
./qvec.py --in_vectors  ${your_vectors} --in_oracle  oracles/semcor_noun_verb.supersenses    
```
To obtain vector column labels, add the --interpret parameter; to print top K values in each dimension add --top K: 

```py
./eval.py --in_vectors ${your_vectors} --in_oracle semcor_noun_verb.supersenses --interpret --top 10
```


#### Syntactic content evaluation: 

```py
./qvec.py --in_vectors  ${your_vectors} --in_oracle  oracles/semcor_noun_verb.supersenses    
```




### Citation:
    @InProceedings{qvec:enmlp:15,
    author = {Tsvetkov, Yulia and Faruqui, Manaal and Ling, Wang and Lample, Guillaume and Dyer, Chris},
    title={Evaluation of Word Vector Representations by Subspace Alignment},
    booktitle={Proc. of EMNLP},
    year={2015},
    }

This repository is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/
