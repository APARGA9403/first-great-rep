
def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(101)
    3
    """
    import math
    
    return math.ceil(n/50)

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.9])
    (0.9, 0)
    >>> stock_price_summary([-0.7])
    (0, -0.7)
    >>> stock_price_summary([-0.3, 1.4])
    (1.4, -0.3)
    >>> stock_price_summary([0.3, 0.4, 0.5])
    (1.2, 0)
     
    """
    tuple_changes = ()
    gains = 0
    losses = 0
    for value in price_changes:
        if value >= 0:
            gains = gains + value
        else:
            losses = losses + value
    return (gains, losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1]
    >>> swap_k(nums, 1)
    >>> nums
    [1]
    >>> nums = [1, 'b']
    >>> swap_k(nums, 1)
    >>> nums
    ['b', 1]
    >>> nums = [1, 2, 6]
    >>> swap_k(nums, 1)
    >>> nums
    [6, 2, 1]
      
    """
    
    L2 = L[0 : k ]
    L3 = L[len(L)-k : ]

    y = 0
    for i in range (len(L3)):
        L[y] = L3[i]
        y =y+1
    
    x= len(L)-k 
    for j in range(len(L2)):
        L[x] = L2[j]
        x = x+1

if __name__ == '__main__':
    import doctest
    doctest.testmod()



