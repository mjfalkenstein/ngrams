# N-Grams Coding Exercise
This is the implementation of the n-grams coding exercise, including some testing and test data. 

## Requirements and Building
This program requires Python 3.X, and was developed and tested using a Python 3.6 virtual environment.
Simply clone this repo into the directory of your choice; no further building should be necessary, as no external libraries are used. 

## Running
Make sure you cd into the git repo directory, then run: 
```
python3 ngrams.py <path/to/input/data.txt> <max_ngrams_length>
```
For example:
```
python3 ngrams.py test_data/test1.txt 2
```
This should yield the following output:
```
a 2
fun 1
good 1
is 1
puzzle 2
a fun 1
a good 1
fun puzzle 1
good puzzle 1
is a 1
puzzle is 1
--- process finished in 0.0005331039428710938 seconds ---
```
