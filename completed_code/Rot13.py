def rot13(message):
    enc_msg = ''
    cypher_key ={
        'A':'N',
        'B': 'O',
        'C': 'P',
        'D': 'Q',
        'E': 'R',
        'F': 'S',
        'G': 'T',
        'H': 'U',
        'I': 'V',
        'J': 'W',
        'K': 'X',
        'L': 'Y',
        'M': 'Z',
        'N': 'A',
        'O': 'B',
        'P': 'C',
        'Q': 'D',
        'R': 'E',
        'S': 'F',
        'T': 'G',
        'U': 'H',
        'V': 'I',
        'W': 'J',
        'X': 'K',
        'Y': 'L',
        'Z': 'M',
        'a':'n',
        'b':'o',
        'c':'p',
        'd':'q',
        'e':'r',
        'f':'s',
        'g':'t',
        'h':'u',
        'i':'v',
        'j':'w',
        'k':'x',
        'l':'y',
        'm':'z',
        'n':'a',
        'o':'b',
        'p':'c',
        'q':'d',
        'r':'e',
        's':'f',
        't':'g',
        'u':'h',
        'v':'i',
        'w':'j',
        'x':'k',
        'y':'l',
        'z':'m',
    }

    for char in message:
        if char in cypher_key:
            enc_msg += cypher_key[char]
        else:
            enc_msg += char

    return enc_msg

# story:
# create a dictionary for the letters to be mapped to 13->
# keep numbers the same as well as symbols
# concatenate to encryption text

if __name__ == '__main__':
    print(rot13('Test'))

# alternative solutions:
'''
import string

def rot13(message):
    lc = string.ascii_lowercase 
    uc = string.ascii_uppercase
    lookup = string.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
    return message.translate(lookup)
'''