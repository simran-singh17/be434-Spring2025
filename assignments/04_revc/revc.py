#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-02-18
Purpose: Print the reverse complement of DNA
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
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

    dna = args.positional
    dna = dna.upper()
    dna = dna.replace('T', 'U')
    dna = dna[::-1]
    for base in dna:
        if base in counts:
            counts[base] += 1

    print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')



# --------------------------------------------------
if __name__ == '__main__':
    main()
