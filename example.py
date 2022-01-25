def sum_items(L):
    """ (list of number) -> number
  
    Return the sum of the items in L.
    >>> lista[1]
    1
    >>> lista[0,0,2]
    2
    >>> lista[1,2]
    3
    >>> lista[1,0,1]
    2
    >>> lista[]
        
    """

    total = 0
    for item in L:
        total = item

    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
