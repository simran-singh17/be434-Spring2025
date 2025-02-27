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
    
    # Define the complement mapping
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    
    # Get the input DNA and ensure it's uppercase
    dna = args.positional.upper()
    
    # Reverse the string
    dna_reversed = dna[::-1]
    
    # Complement each base
    dna_reverse_complement = ''.join([complement.get(base, base) for base in dna_reversed])
    
    # Print the result
    print(dna_reverse_complement)



# --------------------------------------------------
if __name__ == '__main__':
    main()
