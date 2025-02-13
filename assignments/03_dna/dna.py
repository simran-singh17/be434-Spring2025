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
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for base in args.positional:
        if base in counts:
            counts[base] += 1
            
    print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
