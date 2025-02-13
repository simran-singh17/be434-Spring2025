#!/usr/bin/env python3
"""
Author : Simran Singh <Add your email>
Date   : 2025-02-13
Purpose: accept a sequence of DNA as a single positional argument to count tetranucleotide frequency.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
        metavar='DNA',
        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in args.positional:
        jumper[char] += 1
        
    print(args.text.translate(str.maketrans(jumper)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
