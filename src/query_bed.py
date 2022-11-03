"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    read_bed_file, print_line, BedLine
)
from bounds import lower_bound


def extract_region(features: list[BedLine],
                   start: int, end: int) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""
    # FIXME: We want the actual region, not an empty list!

    list_region = []
    for elements in features:
        list_region.append(elements[1])
    start, end = lower_bound(list_region, start), lower_bound(list_region, end)
    
    return features[start:end]

    # low high parameters for binary search
#    low, high = 0, len(features)

    # the recursive case
#    if low > high:
#        return False
#    else:
#        mid = (low + high) // 2
#        if start == mid:
#           return mid
#        elif start > mid:
#            return extract_region(features[mid += 1], start, end)
#        else:
#            return extract_region(features[mid -= 1], start, end)

    
    # lets do a binary search!
    #base case
#    if len(features) <= 1:
#        return features[:]

    # split the list of lists
#    middle = len(features) // 2
#    left = features[:middle:]
#    right = features[middle::]

#    extract_region(left)
#    extract_region(right)

    # file extraction in O(n) no binary search.
#    listMF = []
#    for chrom_features in features:
#        listMF.append[chrom_features[1:3]]
#    return listMF  

def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features = read_bed_file(args.bed)
    for query in args.query:
        chrom, start, end = query.split()
        # Extract the region from the chromosome, using your extract_region()
        # function. If you did your job well, this should give us the features
        # that we want.
        region = extract_region(
            features.get_chrom(chrom), int(start), int(end))
        for line in region:
            print_line(line, args.outfile)


if __name__ == '__main__':
    main()
