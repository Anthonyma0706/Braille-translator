
from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'


####################################################
# Here are two helper functions to get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text

def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    after_word = whole_word_contractions(text) # we convert the word contraction first
    after_all = two_letter_contractions(after_word) # then convert the double contraction
    return after_all


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # replace all straight quotation mark into open quotations
    text = text.replace('"', '“')
    is_open = True 
    newtext = ''
    for char in text:
        if char == '“' and is_open:
            is_open = False
        # this differentiates whether the open quotation exits before it
            newtext += char
        elif char == '“' and not is_open:
            char = '”' # change it to closed quotation mark
            is_open = True # change this condition again so in the next iteration
            newtext += char # if it is '“', we can proceed correctly
        elif char != '“':
            newtext += char
    
    return newtext 


####################################################
# Put your own helper functions here!
def convert_digit_pattern(text):
    """
    (str) -> str
    input the unicode form of the braille string and convert the digit pattern
    to English form from French braille

    >>> convert_digit_pattern('⠼⠃⠼⠚⠼⠃') # this is from text: '202'
    '⠼⠃⠚⠃⠰'
    >>> convert_digit_pattern('⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠚⠼⠃⠉⠕⠍⠏') # COMP 202comp
    '⠨⠨⠉⠕⠍⠏ ⠼⠃⠚⠃⠰⠉⠕⠍⠏'
    """
    newtext = ''
    for i, c in enumerate(text):
        if (c == '⠼' and (i == 0 or i == 1)) or (c == '⠼' and text[i-2] != '⠼'):
            newtext += c # c is the sign of first digit, so keep it
        elif c == '⠼':
            newtext = newtext # not include it since it's not the first sign
        elif (text[i-1:] == '⠼' + c) or (text[i-1] == '⠼' and text[i+1] != '⠼'):
            # this implies this c is the last digit in a certain segment
            # (not necessarily the last in string)
            # so add ⠰ at the end
            newtext += c + '⠰'
        else: # when it's neither unicode of digit nor related to digit, add it
            newtext += c
    return newtext
def convert_parentheses(text):
    """
    (str) -> str
    Replace the open and closed parentheses with '"' to change the pattern for parentheses

    >>> convert_parentheses('(abc)')
    '"abc"'
    >>> convert_parentheses('ar6(4)3')
    'ar6"4"3'
    """
    newtext = ''
    for char in text:
        if char == '(' or char == ')':
            newtext += '"'
        else:
            newtext += char
    return newtext
    
def convert_quotation(text):
    """
    (str) -> str
    convert the '“' and '”' to the parenthese in the original text since the open and closed
    parentheses correspond to the exact pattern of the quotation in English version
    >>> convert_quotation('“ ”o“ ”i“ ”')
    '( )o( )i( )'
    >>> convert_quotation('“Hi” and “Hello”')
    '(Hi) and (Hello)'
    """
    newtext = ''
    for char in text:
        if char == '“':
            newtext += '('
        elif char == '”':
            newtext += ')'
        else:
            newtext += char
    return newtext          
        
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # convert quotes first by calling previous function
    text_quote = convert_quotes(text)
    # convert quotation and parenthese in input
    text_covert_parenthese = convert_parentheses(text_quote)
    text_quotation = convert_quotation(text_covert_parenthese) # NOTE: we convert ? at the end in terms of unicode
    
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text_quotation)
    
    # Run the text through the French Braille translator
    text = text_to_braille(text)

    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))

    # convert the digit pattern
    text = convert_digit_pattern(text)
    # convert the ? pattern in terms of unicode
    text = text.replace('⠢', '⠦')
    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
