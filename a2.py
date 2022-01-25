def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1)>len(dna2):
        return True
    return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2)> 0:
        return True
    return False

def is_valid_sequence(dna) :
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no
    characters other than 'A','T','C' and'G')

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGC12')
    False
    >>> is_valid_sequence('aAtTCGGC')
    False

    """
    x = 0
    y = 0
    for nucleotide in dna:
        if not nucleotide in 'ATCG':
            x = x+1     
    if x > 0:
        return False
    return True

def insert_sequence(dna1, dna2, ind):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.
    The first two parameters are DNA sequences and the third parameter is an index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'    
    >>> insert_sequence('AACGGTT', 'GTT', 5)
    'AACGGGTTTT'  

    """
    dna1 = dna1[:ind] + dna2 + dna1[ind:]
    return dna1

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.
    The first parameter is a nucleotide

    >>> get_complement('A')
       
    >>> get_complement('A')     

    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C' 
    

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    The parameter is a DNA sequence. 

    >>> get_complementary_sequence('AT')
    'TA'    
    >>> get_complementary_sequence('ATCGGC')
    'CGGCTA'  

    """
    x = -1
    complementary_seq = ""
    for char in dna:
        complementary_seq =  complementary_seq +(dna[x])
        x = x - 1
    return  complementary_seq
        
        
    



   

            
         
             


