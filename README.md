# N-Gram Counter
A workflow using Alteryx, Python and Tableau to extract and analyse n-grams from a large set of raw email text.

## Contents
* 'ngram.py' - Python algorithm for n-gram generation.
* 'ngrams.csv' - CSV file containing the generated n-grams.
* 'Parse ngrams.yxmd' - Alteryx workflow to parse and prepare generated n-grams, including dictionary check.

## Resources
* [Elegant n-gram generation in Python](http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/) - A simple n-gram algorithm using zip()
* [English-words](https://github.com/dwyl/english-words) - A text file containing 335k English words
* [Counter class in Python](https://docs.python.org/3/library/collections.html#collections.Counter) - Used to calculate n-gram counts
