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
from collections import OrderedDict

name = sys.argv[1:][0]+".filter.output"
f2 = io.open(name, "w", encoding="utf-8")

def main():
    for filename in sys.argv[1:]:
        print('Processing', filename)
        word_freqs = OrderedDict()
        with open(filename, 'r') as f:
            for line in f:
                words_in = line.strip().split()
                if len(words_in) > 12 and len(words_in) < 80:
                # if len(line) > 12 and len(line) < 240:
                    if line not in word_freqs and "http" not in line:
                        word_freqs[line] = 0
        for line in word_freqs:
            f2.write(line.strip()+"\n")

    print('Done')

if __name__ == '__main__':
    main()
