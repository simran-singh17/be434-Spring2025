#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-03
Purpose: Compute GC content
"""

import argparse
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                    metavar='FILE',
                    nargs='?',
                    default=[sys.stdin],
                    type=argparse.FileType('rt'),
                    help='Input sequence file')

    return parser.parse_args()   



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for sequence in SeqIO.parse(args.file, 'fasta'):
        gc = 0 
        for base in sequence.seq:
            if base == 'G' or base == 'C':
                gc += 1

        print(f'{sequence.id} {gc / len(sequence.seq) * 100:.6f}')
            
   

# --------------------------------------------------
if __name__ == '__main__':
    main()
