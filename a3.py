"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TOO'], 'TO')
    False
    """
    for i in range (len(wordlist)):
        if word == wordlist[i]:
            return True
    return False
          

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    """
    string = ''
    list1 = board[row_index]
    for i in range(len(list1)):
        string = string + list1[i]
    return string


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return all of the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """

    string = ''
     
    for sub_list in board:
        for sub_char in range(len(sub_list)):
            if sub_char == column_index:
                string = string + sub_list[sub_char]
    return string 
                   

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """
    
    list2 = []
    for index in range(len(board)):
        string = make_str_from_row(board, index)
        list2.append(string)
        
    for item in list2:
        if word in item:
            return True
    return False

def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    list3 = []
    for index in range(len(board)-(len(board)-1)):
        for item in range(len(board[index])):
            string = make_str_from_column(board, index)
            list3.append(string)
            index = index+1
              
    for item in list3:
        if word in item:
            return True
    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    inside_row = board_contains_word_in_row(board, word)
    inside_column = board_contains_word_in_column(board, word)

    if inside_row == True:
        return True
    elif inside_column == True:
        return True
    else:
        return False

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    if len(word) < 3:
        points = 0
        return points
    elif len(word) >= 3 and len(word)<= 6:
        points = len(word)*1
        return points
    elif len(word) >= 7 and len(word)<= 9:
        points = len(word)*2
        return points
    else:
        points = len(word)*3
        return points
    

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    points = word_score(word)
    player_info[1] = player_info[1] + points
    print (player_info)
        
    
    
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    check = 0
    for item in words:
        words_in_board = board_contains_word(board, item)
        if words_in_board == True:
            check = check + 1
    return check


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    lista = words_file.readlines()
    
    new_list = []    
    for item in lista:
        new_list.append(item.strip())        
    return new_list
    

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    lista = board_file.readlines()
    
    new_list = []    
    for item in lista:
        new_list.append(item.strip())

    final_list = list(map(list,new_list))
    
    return final_list

     
              

        

  
    
        
        
    
        
        

    
    
