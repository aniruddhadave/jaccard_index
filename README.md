# jaccard_index
Jaccard Index Computation

This package provides computation Jaccard Index based on n-grams for strings. This can be used as a metric for computing similarity between two strings e.g. Indentity resolution

## Installation

Install using pip:
```
#  pip install jaccard-index 
```
To install using the archive, unpack it and run:
```
# python setup.py install
```

## Usage

A common use case is to compare strings for similarity:
```
>>> from jaccard_index.jaccard import jaccard_index
>>> jaccard_index("abc","")
0
>>> jaccard_index("accessary", "accessory")
0.6
>>> jaccard_index("coffee", "coffee")
1
```