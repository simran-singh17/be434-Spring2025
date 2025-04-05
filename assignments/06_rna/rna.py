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

    if not os.path.isdir(args.outfile):
        os.makedirs(args.outfile)

    rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'} 
    
    
    #add counter for files 
    for fh in args.file:
        for line in fh:
            #this will be the sequences, add a counter 
            #add something to make all caps 
            line = line.strip()
            rna_line = ''.join([rna.get(base, base) for base in line])
        print(rna_line, file=args.positional) #print the DNA to RNA results to the out directory 

#print(f'Done, wrote {num_seqs} sequences in {num_files} files to directory "{out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
