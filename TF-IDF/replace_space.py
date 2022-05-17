from __future__ import print_function
from pickle import encode_long

import numpy

try:
    import cPickle as pkl
except:
    import pickle as pkl

import sys
import fileinput
import io

name = sys.argv[1:][0]+".output"
f2 = io.open(name, "w", encoding="utf-8")

def main():
    for filename in sys.argv[1:]:
        print('Processing', filename)
        with open(filename, 'r') as f:
            for line in f:
                words_in = line.strip().replace(" ", "")
                f2.write(words_in+"\n")

    print('Done')

if __name__ == '__main__':
    main()
