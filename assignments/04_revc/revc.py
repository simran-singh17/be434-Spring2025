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
  
    args = parser.parse_args()                                         
  
    if os.path.isfile(args.positional):    
        args.positional = open(args.positional).read().rstrip()
                   

    return args
    
    

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a' }
    dna = args.positional
    dna_reversed = dna[::-1]
    dna_reverse_complement = ''.join([complement.get(base, base) for base in dna_reversed])
    print(dna_reverse_complement)



# --------------------------------------------------
if __name__ == '__main__':
    main()
