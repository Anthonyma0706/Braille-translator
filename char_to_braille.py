from helpers import *

# More constants you'll want to use:
SPACE = '..\n..\n..'
HYPHEN = '..\n..\noo' 
APOSTROPHE = '..\n..\no.' 
QUOTES = '..\noo\noo'


############################ Functions

def convert_irregular(c):
    '''(str) -> str
    Convert the irregular characters to French Braille.
    Recall these are: space, hyphen, apostrophe, guillements
    Apostrophe could be represented by `, ’ or '.
    Hyphen could be represented by - or by –.
    Note the constants such as SPACE and HYPHEN above.

    >>> print(convert_irregular('-'))
    ..
    ..
    oo
    >>> convert_irregular('–')
    '..\\n..\\noo'
    >>> convert_irregular('`')
    '..\\n..\\no.'
    >>> convert_irregular("'")
    '..\\n..\\no.'
    >>> convert_irregular("’")
    '..\\n..\\no.'
    >>> convert_irregular("»")
    '..\\noo\\noo'
    '''
    # Here we progressively check if c corresponds to any of the symbol of irregular char
    # Then assign the corresponding constant to c
    # Finally, return c
    if c == ' ':
        c = SPACE
    elif c == '–' or c == '-':
        c = HYPHEN
    elif c == '`' or c == "'" or c == "’":
        c = APOSTROPHE
    elif c == "»" or c == "«":
        c = QUOTES
        
    return c

def decade_pattern(decade_position):
    '''(int) -> str
    Using position in Braille decade, get associated Braille pattern.
    Provided to students. Do not edit this function.

    >>> decade_pattern(0)
    'o.\\n..'
    >>> decade_pattern(9)
    '.o\\noo'
    '''
    DEC_SEQ = ['o.\n..', 'o.\no.', 'oo\n..', 'oo\n.o',
           'o.\n.o', 'oo\no.', 'oo\noo', 'o.\noo',
           '.o\no.', '.o\noo']
    return DEC_SEQ[decade_position]


def convert_digit(c):
    '''(str) -> str
    Convert string representation of digit
    to Braille. For this, put the decade value in the top two rows,
    and put '..' in the bottow row.
    Hints:
        - Remember: we provided the string DIGITS to you
        - For full credit, this should have fewer than 4 lines of code.

    >>> print(convert_digit('1'))
    o.
    ..
    ..
    >>> print(convert_digit('3'))
    oo
    ..
    ..
    >>> print(convert_digit('0'))
    .o
    oo
    ..
    >>> print(convert_digit('a'))
    None
    '''
    # first, if c is not digit, return None
    # The function decade_pattern(decade_position) gives us the pattern
    # and its input is exactly the index.
    # So we need to find the index of c in string DIGITS using find method
    # then concatenate "\n.." at the end to convert pattern succesfully
    if not is_digit(c):
        return # this returns None
    return decade_pattern(DIGITS.find(c)) + "\n.."
 
          
   
def convert_punctuation(c):
    '''(str) -> str
    Convert string representation of common punctuation
    to French Braille. For this put the decade value in the bottom
    two rows, and put '..' in the top row.
    Hints: 
        - Use the string PUNCTUATION we provided to you
        - Recall there are helper functions we gave you
        - For full credit, this should have fewer than 4 lines of code.
        - You should not have to manually enter any Braille strings

    >>> print(convert_punctuation(','))
    ..
    o.
    ..
    >>> print(convert_punctuation(';'))
    ..
    o.
    o.
    >>> print(convert_punctuation(':'))
    ..
    oo
    ..
    >>> print(convert_punctuation('"'))
    ..
    oo
    oo
    '''
    # first, if c is not punctuation, return None
    # The function decade_pattern(decade_position) gives us the pattern
    # and its input is exactly the index.
    # So we need to find the index of c in string PUNCTUATION using find method
    # then concatenate "..\n" at the beginning to convert pattern succesfully
    if not is_punctuation(c):
        return
    return "..\n" + decade_pattern(PUNCTUATION.find(c)) 
    


############################# 


def decade_ending(dec_num):
    '''(int) -> str
    For one of the four decades of standard letters in French Braille,
    return the associated bottom-row (see page 3 of pdf.)

    >>> decade_ending(0)
    '..'
    >>> decade_ending(1)
    'o.'
    >>> decade_ending(2)
    'oo'
    >>> decade_ending(3)
    '.o'
    '''
    # return the corresponding pattern one by one
    if dec_num == 0:
        ending = '..'
    elif dec_num == 1:
        ending = 'o.'
    elif dec_num == 2:
        ending = 'oo'
    elif dec_num == 3:
        ending = '.o'
    return ending

def letter_row(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    the number of the decade it belongs to. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_row('a')
    0
    >>> letter_row('w')
    3
    >>> letter_row('n')
    1
    >>> letter_row('N')
    1
    '''
    c = c.lower() # convert
    for i, decade in enumerate(LETTERS):
        if c in decade:
            return i


def letter_column(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    its position within its decade. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_column('a')
    0
    >>> letter_column('b')
    1
    >>> letter_column('v')
    1
    >>> letter_column('w')
    9
    >>> letter_column('W')
    9
    '''
    c = c.lower() # convert
    for decade in LETTERS:
        if c in decade:
            return decade.find(c)


def convert_letter(c):
    '''(str) -> str
    For one of the standard letters in French Braille,
    return its Braille representation.

    >>> print(convert_letter('a'))
    o.
    ..
    ..
    >>> print(convert_letter('b'))
    o.
    o.
    ..
    >>> print(convert_letter('p'))
    oo
    o.
    o.
    >>> print(convert_letter('ç'))
    oo
    o.
    oo
    >>> print(convert_letter('ô'))
    oo
    .o
    .o
    >>> print(convert_letter('A'))
    o.
    ..
    ..
    >>> print(convert_letter('Œ'))
    .o
    o.
    .o
    '''
    c = c.lower() # convert c to lowercase
    # letter_column function gives us the index actually
    # letter_row gives us the number of decade, which we need to find the ending pattern
    main_pattern = decade_pattern(letter_column(c))
    end_pattern = decade_ending(letter_row(c))
    if not is_letter(c):
        return
    return main_pattern + "\n" + end_pattern


def char_to_braille(c):
    '''(str) -> str
    Convert a character, c, into French Braille.
    If c is a character we don't know how to convert, return 
    the same character as before.

    >>> print(char_to_braille('-'))
    ..
    ..
    oo
    >>> print(char_to_braille('w'))
    .o
    oo
    .o
    >>> print(char_to_braille('1'))
    o.
    ..
    ..
    >>> print(char_to_braille('?'))
    ..
    o.
    .o
    >>> char_to_braille('.')
    '..\\noo\\n.o'
    >>> char_to_braille('a')
    'o.\\n..\\n..'
    >>> char_to_braille('n')
    'oo\\n.o\\no.'
    >>> char_to_braille('Z')
    'o.\\n.o\\noo'
    >>> char_to_braille('Œ')
    '.o\\no.\\n.o'
    >>> char_to_braille(' ')
    '..\\n..\\n..'
    >>> char_to_braille('ß')
    'ß'
    >>> char_to_braille('\\n')
    '\\n'
    '''
    c = c.lower() # convert, then it includes capitalized letter
    # check one by one, using the helper functions
    if is_irregular(c):
        c = convert_irregular(c)
    elif is_digit(c):
        c = convert_digit(c)
    elif is_punctuation(c):
        c = convert_punctuation(c)
    elif is_letter(c):
        c = convert_letter(c)
    # If c is a character we don't know how to convert, return 
    # the same character as before.
    elif not is_known_character(c):
        c = c
    
    return c

if __name__ == '__main__':
    doctest.testmod()
