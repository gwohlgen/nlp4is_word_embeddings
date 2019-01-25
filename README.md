# A Dataset for Relations in Digital Humanities and its Evaluation with Word Embeddings

Dependencies:
* `gensim-2-1-0` (or higher)

### Summary
Here you find the following:
* **2 datasets** for evaluating language models about the books **A Song of Ice and Fire** (GRR Martin) 
* The dataset contains a large of number of task of type **analogy** and **doesnt-match**.
* Your model can be tested easily, especially if it is of type KeyedVector, ie. a [Gensim](https://radimrehurek.com/gensim) Word-Vectors model (eg. create with word2vec).
* Furthermore, here you find scripts to create / extend the datasets -- by creating permutations of input data.
* Finally, you can re-use the scripts to evaluate the data.

 
## The Datasets
The datasets can be found in the folder [datasets](datasets).
Like in the original word2vec-toolkit, the files to be evaluated are named `questions`\*.
There are four datasets:
* `datasets/questions_soiaf_analogies.txt`: Analogies relation test data for *A Song of Ice and Fire*
* `datasets/questions_soiaf_doesn_match.txt`: Doesnt_match task test data for *A Song of Ice and Fire*

If you want to extend or modify the test data, edit the respective source files in the folder [datasets](datasets):
`soiaf_analogies.txt`,`soiaf_does_not_match.txt`.

After modifying the test data run the following command to re-create the datasets.
```
    cd datasets 
    python create_questions.py
```

This will generate section-based permutations to create the evaluation datasets. 


## The Models
To evaluate the datasets you need language models, examples of which are provided in the folder [models](models)
(or you can use your own strategies).

We used different well-known techniques to create word-embedding models, for example word2vec, GloVe, fastText, and LexVec. 
The models having names staring with `asoif_` are trained on the first for books of *A Song of Ice and Fire*,
and the models starting with `hp_` are trained on the complete *Harry Potter*. For copyright reasons the plain-text of
the books can not be included here.

For more details on the models and the parameters used for training, see [models/README.md](models/README.md).

## Doing the evalation

Choose the book series you want to evaluate (`asoif` or `hp`), and the task type you want to
do, analogy or doesnt_match. Call the scripts as shown below.


#### Analogies task
```
    cd src
    python analogies_evaluation.py asoif        # to eval A Song of Ice and Fire book series
    python analogies_evaluation.py hp           # to eval Harry Potter book series
```

#### Doesnt_match task
```
    cd src
    python doesnt_match_evaluation.py hp        # to eval Harry Potter book series
    python doesnt_match_evaluation.py asoif     # to eval A Song of Ice and Fire book series

```

The output of the scripts will be various count (how many tasks per section, how many correctly and incorrectly solved,
and the percentage (accuracy) of correct suggestions).


## Finally: For adding new dataset or models
We tried to make the system easily extendable to evaluate new models.

* Adding models: just put them into the [models](models) folder, and add them into the `METHODS` variable in `config.py`.
* Adding new datasets and models: add the raw dataset into [datasets](datasets), generate the `questions`. Add a new section to `config.py` with the settings for 
the new dataset. Also add new models, probably (see above).


## Student datasets / repos:
For *Witcher* dataset for Polish language books and datasets, see [here](https://github.com/Ba-Ski/nlp4is_word_embeddings)

