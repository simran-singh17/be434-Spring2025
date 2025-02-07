#!/usr/bin/env python3
"""
Author : Simran
Date   : 2025-02-07
Purpose: say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='A Greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='A name to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='If included print !',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited

    phrase = ''
    if excited:
        phrase = greeting + ', ' + name + '!'
    else:
        phrase = greeting + ', ' + name + '.'

    print(phrase)
   

# --------------------------------------------------
if __name__ == '__main__':
    main()
