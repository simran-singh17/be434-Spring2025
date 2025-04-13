#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-04-02
Purpose: Parsing Delimited Text Files
"""

import argparse
import sys
import os
import re
import csv



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-b FILE',
                       '--blasthits FILE',
                       help='BLAST -outfmt 6',
                       metavar='FILE',
                       type=argparse.FileType('rt'),
                       default=None)

    parser.add_argument('-a FILE',
                        '--annotations FILE',
                        help='BLAST -outfmt 6',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                    '--outfile',
                    help='Output file',
                    metavar='FILE',
                    type=argparse.FileType('wt'),
                    default='out.txt')

    parser.add_argument('-d DELIM',
                        '--delimiter DELIM',
                        help='Output field delimiter',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="")

    parser.add_argument('-p PCTID',
                        '--pctid PCTID',
                        help='Output field delimiter',
                        metavar='Percent',
                        type=int,
                        default=0.0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    infile= args.blasthits


# --------------------------------------------------
if __name__ == '__main__':
    main()
