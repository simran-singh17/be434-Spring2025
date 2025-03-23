#!/usr/bin/env python3
"""
Author : Simran Singh <singh17@arizona.edu>
Date   : 2025-03-03
Purpose: Compute GC content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                    metavar='FILE',
                    nargs='*',
                    default=[sys.stdin],                             
                    type=argparse.FileType('rt'),                    
                    help='Input sequence file')

    return parser.parse_args()   



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout   
    out_fh.write(args.text.upper() + '\n')                              
    out_fh.close() 
    
    args.file = [open(fh) for fh in args.file]
    num_files, num_lines, num_chars = 0, 0, 0
    for fh in args.file:
        num_files += 1
        for line in fh:
            num_lines += 1
            num_chars += len(line)
            print(f'{fh.name}: {line.upper().count("G") + line.upper().count("C")}', file=out_fh)
   

# --------------------------------------------------
if __name__ == '__main__':
    main()
