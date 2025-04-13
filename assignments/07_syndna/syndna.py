#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-23
Purpose: Create synthetic sequences
"""

import argparse
import sys
import random
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

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
             def generate_sequence(seq_type, length, gc_content):
                 """Generate random sequence with a specified GC content."""
                 bases = "ACGT" if seq_type == "dna" else "ACGU"

                 while True:
                     seq = "".join(random.choices(bases, k=length))
                     gc = gc_fraction(seq) / 100
                     if abs(gc - gc_content) <= 0.05:
                         break
                 return seq

def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""

    t_or_u = "T" if seq_type == "dna" else "U"
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = "A" * num_at + "C" * num_gc + "G" * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return "".join(sorted(pool))

def test_create_pool():
    """Test create_pool"""

    state = random.getstate()
    random.seed(1)
    assert create_pool(0.5, 10, "dna") == "AAACCCGGTT"
    assert create_pool(0.6, 11, "rna") == "AACCCCGGGUU"
    assert create_pool(0.7, 12, "dna") == "ACCCCCGGGGGT"
    assert create_pool(0.7, 20, "rna") == "AAACCCCCCCGGGGGGGUUU"
    assert create_pool(0.4, 15, "dna") == "AAAACCCGGGTTTTT"
    random.setstate(state)

def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(args.numseqs):
        length = random.randint(args.minlen, args.maxlen)
        seq = "".join(random.sample(pool, length))
        j = i + 1
        args.outfile.write(f">{j}\n{seq}\n")

    print(
        f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile.name}".'
    )

# --------------------------------------------------
if __name__ == '__main__':
    main()
