"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line, BedLine
)


def read_bed_file(f: TextIO) -> list[BedLine]:
    """Read an entire sorted bed file."""
    # Handle first line...
    line = f.readline()
    if not line:
        return []

    res = [parse_line(line)]
    for line in f:
        feature = parse_line(line)
        prev_feature = res[-1]
        assert prev_feature.chrom < feature.chrom or \
            (prev_feature.chrom == feature.chrom and
             prev_feature.chrom_start <= feature.chrom_start), \
            "Input files must be sorted"
        res.append(feature)

    return res



def merge(f1: list[BedLine], f2: list[BedLine], outfile: TextIO) -> None:
    """Merge features and write them to outfile."""
    # FIXME: I have work to do here!
    # her skal jeg loope igennem chrom start like so f1[i][0] and f2[j][0]
    i,j = 0,0
    bed_merged = []
    while i < len(f1) or j < len(f2):
        if f1[i][0] < f2[j][0]:
            bed_merged.append(f1[i])
            i += 1
        else: # f2[j] < f1[i]
            bed_merged.append(f2[j])
            j += 1

# Logically written, so i can remember what I am doing   
#    if f1[i] == len(f1[i]):
#        bed_merged += f2[j::]
#    else:
#        bed_merged += f1[i::]

    # the short version
    bed_merged += f1[i::] + f2[j::]
    print_line(bed_merged, outfile)
    return outfile



def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Merge two BED files")
    argparser.add_argument('f1', type=argparse.FileType('r'))
    argparser.add_argument('f2', type=argparse.FileType('r'))
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',   # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features1 = read_bed_file(args.f1)
    features2 = read_bed_file(args.f2)
    merge(features1, features2, args.outfile)


if __name__ == '__main__':
    main()
