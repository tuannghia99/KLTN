# from tfidf import TfIdf

# import tfidf
from __future__ import unicode_literals
from tfidf import TfIdf


"""
compute IF-IDF  .

Run: python compute_IF_IDF -i test.en -v vocab -o out.en 

"""



import sys
import codecs
import re
import copy
import argparse
from collections import defaultdict, Counter
import collections

# hack for python2/3 compatibility
import sys
import codecs
import re
import copy
import argparse
from collections import defaultdict, Counter
import collections

# hack for python2/3 compatibility
from io import open
import threading
import time
import operator

argparse.open = open

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Extract parallel from WIT")
    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text (default: standard input) need to compute IF-IDF.")

    parser.add_argument(
        '--vocab', '-v', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text - vocab indomain file (default: standard input)")

    parser.add_argument(
        '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file contain similarity score (default: standard output)")
    return parser




def main(infile,vocab, outfile):
    i=0
    dict = []
    for line in vocab:
        # print(line)
        dict.append(line.strip())  #". " -vi
    #
    # print(vocab)
    table = TfIdf()
    table.add_document("indomain", dict)

    scores = []
    sent_id=0
    for line in infile:
        words=line.strip().split()

        # print(table.similarities(words))
        scores.append((table.similarities(words)[0][1], sent_id))
        sent_id=sent_id+1
        if sent_id % 10000 ==0:
            print("Number sents:",sent_id)

    sorted_sens=[i[1] for i in sorted(scores)]

    # print(sorted_sens[::-1])

    top=sorted_sens[::-1][:200000]

    id=0
    infile.close()

    print("Dump to file..............")
    f= open("/home/ngovinh/NgoVinh/D/NMT2018/Corpus-store/VLSP/MONO_VI/corpus.10M.shuf.tok.true.vi",'r')

    lines=f.readlines()

    print("Lengths: ",len(lines))
    f.close()
    id=0 
    for i  in top:
        # print(line)
        # if i in top:
        outfile.write(lines[i])
        id=id+1
        if id  % 10000 ==0:
            print("Number sents selected:",id )

    # table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g","c", "h"])
    # table.add_document("bar", ["a", "b", "c", "i", "j", "k",])
    # table.add_document("baz", ["k", "l", "m", "n"])
    # table.add_document("baz1", ["a", "b", "c"])
    # print(table.similarities(["a", "b", "c"]))


    infile.close()
    outfile.close()


if __name__ == '__main__':

    # python 2/3 compatibility
    if sys.version_info < (3, 0):
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr)
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        sys.stdin = codecs.getreader('UTF-8')(sys.stdin)
    else:
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer)
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer)
        sys.stdin = codecs.getreader('UTF-8')(sys.stdin.buffer)

    parser = create_parser()
    args = parser.parse_args()

    # read/write files as UTF-8
    if args.input.name != '<stdin>':
        args.input = codecs.open(args.input.name, encoding='utf-8')
    if args.vocab.name != '<stdin>':
        args.vocab = codecs.open(args.vocab.name, encoding='utf-8')

    if args.output.name != '<stdout>':
        args.output = codecs.open(args.output.name, 'w', encoding='utf-8')

    main(args.input, args.vocab, args.output)

