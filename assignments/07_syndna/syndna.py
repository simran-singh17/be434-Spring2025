#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-23
Purpose: Create synthetic sequences
"""

import argparse
import sys
import random
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o str',
                    metavar='--outfile str',
                    nargs='*',
                    default=[sys.stdout],
                    type=argparse.FileType('out.fa'),
                    help= 'Output file')
                    
    parser.add_argument('-t str',
                    '--seqtype str',
                    help='DNA or RNA',
                    metavar='str',
                    type=str,
                    default='dna')

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-n int',
                        '--numseq int',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m int',
                    '--minlen int',
                    help='Minimum length',
                    metavar='int',
                    type=int,
                    default=50)

    parser.add_argument('-x int',
                    '--maxlen int',
                    help='Maximum length',
                    metavar='int',
                    type=int,
                    default=70)
                    
    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
                    
    parser.add_argument('-p float',                                             
                    '--pctgc float',
                    help='--Percent GC',
                    metavar='integers',
                    type=int,
                    default=0.5)
                                

    parser.add_argument('positional', 
                            metavar='DIR',
                            nargs='*',
                            default= [sys.stdout],
                            help='Output directory')
                    
    parser.add_argument('-s',                                            
                    '--seed',
                    help='Random seed',
                    metavar='seed',
                    type=int,
                    default=None)

    return parser.parse_args()


# --------------------------------------------------

def main():
    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    dna_letters = ['A', 'C', 'G', 'T']
    rna_letters = ['A', 'C', 'G', 'U']

def create_pool(pctgc, max_len, seq_type):
    pool = []
    for i in range(args.numseq):
        seq = ''
        if seq_type == 'dna':
            seq = ''.join(random.choices(list(dna_letters), k=random.randint(args.minlen, args.maxlen)))
        elif seq_type == 'rna':
            seq = ''.join(random.choices(list(rna_letters), k=random.randint(args.minlen, args.maxlen)))
        else:
            print('Invalid sequence type')
        pool.append(seq)
    return pool
    
t_or_u = 'T' if seq_type == 'dna' else 'U'
num_gc = int((pctgc / 2) * max_len)        
num_at = int(((1 - pctgc) / 2) * max_len)  
pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at 

for _ in range(max_len - len(pool)):       
                    pool += random.choice(pool)

                    return ''.join(sorted(pool))            




# --------------------------------------------------
if __name__ == '__main__':
    main()
