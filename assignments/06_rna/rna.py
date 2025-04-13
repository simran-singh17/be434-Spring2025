#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-11
Purpose: Transcribe DNA to RNA
"""

import argparse
import sys
import os 


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input DNA file(s)')                                

    parser.add_argument('-o',
                        '--outfile',
                        metavar='DIR',
                        default= [sys.stdout],
                        help='Output directory')

    return parser.parse_args()         

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args() 

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    total_sequences = 0
    file_count = 0

    for filename in args.file:
        with open(filename, 'rt') as fh:
            dna = fh.read().strip()
        rna = dna.replace('T', args.RNA).replace('t', args.RNA.lower())

        sequences = rna.splitlines()
        total_sequences += len(sequences)
        file_count += 1

        out_file = os.path.join(args.out_dir, os.path.basename(filename))
        with open(out_file, 'w') as f:
            f.write('\n'.join(sequences))

    sequence_word = "sequence" if total_sequences == 1 else "sequences"
    file_word = "file" if file_count == 1 else "files"

    print(f'Done, wrote {total_sequences} {sequence_word} in {file_count} {file_word} to directory "{args.out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
