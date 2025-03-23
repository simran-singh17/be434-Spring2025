#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-11
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
        metavar='FILE',
        nargs='*',
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help='Input DNA file')                                

    parser.add_argument('positional', 
        metavar='DIR',
        nargs='*',
        default= [sys.stdout],
        help='Output directory')

    return parser.parse_args()         

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args() 
    dna = args.file
    rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 'u', 'c': 'g', 'g': 'c', 't': 'a'} 
    
    for fh in args.file:
        for line in fh:
            line = line.strip()
            rna_line = ''.join([rna.get(base, base) for base in line])
            print(rna_line, file=args.positional)


# --------------------------------------------------
if __name__ == '__main__':
    main()
