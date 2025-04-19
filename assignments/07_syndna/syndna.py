#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-23
Purpose: Create synthetic sequences
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    if args.seqtype not in ['dna', 'rna']:
        parser.error(f'--seqtype "{args.seqtype}" must be "dna" or "rna"')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    numseqs = args.numseqs
    min_len = args.minlen
    max_len = args.maxlen
    seq_type = args.seqtype
    sequence_type = 'DNA' if seq_type == 'dna' else 'RNA'

    with open(args.outfile, 'w', encoding='utf-8') as out_file:
        for i in range(numseqs):
            seq_len = random.randint(min_len, max_len)
            seq = ''.join(random.sample(pool, seq_len))
            out_file.write(f'>{i+1}\n{seq}\n')

    print(
        f'Done, wrote {numseqs} {sequence_type} sequences '
        f'to "{args.outfile}".'
    )

# --------------------------------------------------
    def create_pool(pctgc, max_len, seq_type):
        """ Create the pool of bases """

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
