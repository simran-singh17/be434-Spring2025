#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-11
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys
import shutil

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='File', nargs='+', help='Input DNA file(s)')

    parser.add_argument('-R',
                        '--RNA',
                        help='Replacement for T (default: U)',
                        metavar='str',
                        type=str,
                        default='U')

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory for RNA sequences',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    for filename in args.file:
        if not os.path.isfile(filename):
            print(f"usage: {sys.argv[0]} <File>", file=sys.stderr)
            print(f"No such file or directory: '{filename}'", file=sys.stderr)
            sys.exit(1)

    return args

# --------------------------------------------------
def main():
    """Convert DNA to RNA"""

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
#pytest -xv test.py

# --------------------------------------------------
if __name__ == '__main__':
    main()