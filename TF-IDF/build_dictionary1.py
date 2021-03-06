from __future__ import print_function

import numpy

try:
    import cPickle as pkl
except:
    import pickle as pkl

import sys
import fileinput

from collections import OrderedDict

def main():
    for filename in sys.argv[1:]:
        print('Processing', filename)
        word_freqs = OrderedDict()
        with open(filename, 'r') as f:
            for line in f:
                words_in = line.strip().split(' ')
                for w in words_in:
                    if w not in word_freqs:
                        word_freqs[w] = 0
                    word_freqs[w] += 1

        words = list(word_freqs.keys())
        freqs = list(word_freqs.values())
        sorted_idx = numpy.argsort(freqs)
	

	
    with open('%s.vocab'%filename, 'wt') as f:
        sorted_words = [words[ii] for ii in sorted_idx[::-1]]
        #f.write("unk"+"\n")
		#f.write("<s>"+"\n")
                #f.write("</s>"+"\n")
        #f.write("".join([words[ii]+" "+ str(freqs[ii]) +"\n" for ii in sorted_idx[::-1]]))
        f.write("".join([words[ii]+"\n" for ii in sorted_idx[::-1]]))
	
      #  worddict = OrderedDict()
      #  worddict['eos'] = 0
     #	worddict['UNK'] = 1
        
     #   for ii, ww in enumerate(sorted_words):
      #      worddict[ww] = ii+2

       # with open('%s.txt'%filename, 'wt') as f:
	#	for ii, ww in enumerate(sorted_words):	
         #   pkl.dump(worddict, f)

    print('Done')

if __name__ == '__main__':
    main()
