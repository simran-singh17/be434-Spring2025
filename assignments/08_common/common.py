#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-30
Purpose: find common words
"""

import argparse
import sys
PRG = './common.py'
FOO = './inputs/foo.txt'
BAR = './inputs/bar.txt'
EXPECTED1 = ['bar', 'foo']


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')
    parser.add_argument('-o  file',
                        metavar='--outfile FILE',
                        nargs='*',
                        default=[sys.stdout],
                        type=argparse.FileType('rt'),
                        help='Output file') 
    parser.add_argument('FILE1',
                        metavar='Input file 1',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input file 1') 
    parser.add_argument('FILE2',
                        metavar='Input file 2',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input file 2') 
                    
    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.FILE1
    file2 = args.FILE2
    outfile = args.outfile
    common_words = [word for word in file1 if word in file2]
    for line1 in file1: 
        line1 = line1.strip()
        for line2 in file2:
            line2 = line2.strip()
            if line1 == line2:
                common_words.append(line1)
    print(common_words, file=outfile)

# --------------------------------------------------
if __name__ == '__main__':
    main()
