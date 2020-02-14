
import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    # create a string constant for the template of binary representation
    eight_bit = '12345678'
    # create an empty string for the following iterations to concatenate with
    binary_string = ''
    for char in eight_bit:
        if char in s: #check each character in the template to see if it
          binary_string += '1' # is in the input number string, if yes, print 1 at this position
        else:
          binary_string += '0'  # if not in, print 0 at this position, as required
    return binary_string # return the final string


def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    # for clarification, call s as binary_str
    binary_str = s
    reverse_binary = binary_str[::-1] # reverse it using slice, take step -1
    # now use built-in function int( , 2) to convert the number in binary stirng to decimal base int
    reverse_decimal = int(reverse_binary, 2)
    # use built-in function hex that takes in a base-10 number
    # and converts it to a string in hexadecimal that starts with `0x'.
    string_hexa = hex(reverse_decimal + int('2800', 16)) # Here, add 2800 in decimal number together
    # remove the first two character since they are not the numbers that we want
    string_hexanumber = string_hexa[2: ]
    return string_hexanumber


def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    # I would like to set up a variable assign boolean expression to it to make the code
    # more readable, but since the length of our input string could be smaller or larger
    # I can only generate them inside the if loop, but the logic is simple:
    # just check each index in its string to see if it's valid
    if  len(s) == 8: # means its length is same as a 6-dot string 
        if s[0] in 'o.' and s[1] in 'o.' and s[2] == '\n' and s[3] in 'o.' and s[4] in 'o.' and s[5] == '\n' and s[6] in 'o.' and s[7] in 'o.':
            return True
        else:
            return False
    elif len(s) == 11: # means its length is same as 8-dot string
        if s[0] in 'o.' and s[1] in 'o.' and s[2] == '\n' and s[3] in 'o.' and s[4] in 'o.' and s[5] == '\n' and s[6] in 'o.' and s[7] in 'o.' and s[8] == '\n' and s[9] in 'o.' and s[10] in 'o.':
            return True
        else:
            return False
    else: # This else includes the length of string that is not 8 or 11, which means it's in not ostring format
        return False
def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    # We do it step by step to convert
    rasied_pos = ostring_to_raisedpos(s)
    binary = raisedpos_to_binary(rasied_pos)
    hex_num = binary_to_hex(binary)
    unicode = hex_to_unicode(hex_num) # now we have the unicode version of s

    if is_ostring(s):
        s = unicode
    else: # as required, if s is not a ostring, return itself
        s = s
    return s


if __name__ == '__main__':
    doctest.testmod()
