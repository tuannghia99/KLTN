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
        '--input1', '-i1', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text (default: standard input) need to compute IF-IDF src")
    parser.add_argument(
        '--input2', '-i2', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text (default: standard input) need to compute IF-IDF tgt")

    parser.add_argument(
        '--vocab1', '-v1', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text - vocab indomain file (default: standard input) src ")

    parser.add_argument(
        '--vocab2', '-v2', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text - vocab indomain file (default: standard input) tgt ")

    parser.add_argument(
        '--output1', '-o1', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file contain similarity score (default: standard output) src")

    parser.add_argument(
        '--output2', '-o2', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file contain similarity score (default: standard output) tgt")
    return parser




def main(infile1, infile2,vocab1,vocab2, outfile1, outfile2):
    i=0
    dict1 = []  # en
    dict2=[]  # vi
    for line in vocab1:
        # print(line)
        dict1.append(line.strip())  #". " -vi

    for line in vocab2:
        # print(line)
        dict2.append(line.strip())  #". " -vi
    #
    # print(vocab)
    table1 = TfIdf()
    table1.add_document("indomain", dict1)

    table2 = TfIdf()
    table2.add_document("indomain", dict2)

    scores = []
    sent_id=0
    for line1,line2 in zip(infile1,infile2):
        words1=line1.strip().split()
        words2=line2.strip().split()

        # print(table.similarities(words))
        scores.append((table1.similarities(words1)[0][1]+table2.similarities(words2)[0][1], sent_id))
        sent_id=sent_id+1
        if sent_id % 10000 ==0:
            print("Number sents scores:",sent_id)

    sorted_sens=[i[1] for i in sorted(scores)]

    # print(sorted_sens[::-1])

    top=sorted_sens[::-1] #[:2000000]

    id=0
    # infile1.close()

    infile1.seek(0)
    infile2.seek(0)

    print("Dump to file..............")
    # f= open("/home/ngovinh/NgoVinh/D/NMT2018/Corpus-store/VLSP/MONO_VI/corpus.10M.shuf.tok.true.vi",'r')

    lines1=infile1.readlines()
    lines2=infile2.readlines()

    print("Lengths: ",len(lines1),'  ', len(lines2))
    # f.close()
    id=0
    for i in top:
        # print(line)
        # if i in top:
        outfile1.write(lines1[i])  #********
        outfile2.write(lines2[i])
        id=id+1
        if id  % 10000 ==0:
            print("Number sents selected:",id )

    # table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g","c", "h"])
    # table.add_document("bar", ["a", "b", "c", "i", "j", "k",])
    # table.add_document("baz", ["k", "l", "m", "n"])
    # table.add_document("baz1", ["a", "b", "c"])
    # print(table.similarities(["a", "b", "c"]))


    infile1.close()
    infile2.close()
    outfile1.close()
    outfile2.close()


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
    if args.input1.name != '<stdin>':
        args.input1 = codecs.open(args.input1.name, encoding='utf-8')
    if args.input2.name != '<stdin>':
        args.input2 = codecs.open(args.input2.name, encoding='utf-8')


    if args.vocab1.name != '<stdin>':
        args.vocab1 = codecs.open(args.vocab1.name, encoding='utf-8')
    if args.vocab2.name != '<stdin>':
        args.vocab2 = codecs.open(args.vocab2.name, encoding='utf-8')

    if args.output1.name != '<stdout>':
        args.output1 = codecs.open(args.output1.name, 'w', encoding='utf-8')

    if args.output2.name != '<stdout>':
        args.output2 = codecs.open(args.output2.name, 'w', encoding='utf-8')

    main(args.input1, args.input2, args.vocab1,args.vocab2, args.output1, args.output2)

