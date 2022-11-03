"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    # FIXME: Obviously the answer isn't always 0
    #So searching through the list for the sequences lowest index for the value 
    low=0
    high=len(x)
    while low < high:
        mid=(high+low)//2
        
        if x[mid] <v:
            low=mid+1
        else:
            high=mid
    return low


def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).

    """
    return lower_bound(x,v+1)
   
    # FIXME: Obviously the answer isn't always 0
