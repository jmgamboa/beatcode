morse_code_values = morse_binary = {
    'a': '0100',
    'b': '1000',
    'c': '1010',
    'd': '1000',
    'e': '0000',
    'f': '0010',
    'g': '1100',
    'h': '0000',
    'i': '0000',
    'j': '0111',
    'k': '1010',
    'l': '0100',
    'm': '1100',
    'n': '1000',
    'o': '1110',
    'p': '0110',
    'q': '1101',
    'r': '0100',
    's': '0000',
    't': '1000',
    'u': '0010',
    'v': '0001',
    'w': '0110',
    'x': '1001',
    'y': '1011',
    'z': '1100'
}

input_string = 'she quick brown fox'
target_string = 0000

output = True

"""
outputstring = "1000000010000000"
                   ^
'the quick brown fox'
  ^

input bits= 1 1
              ^
t = 1000
     ^
return outputstring == target

2 < outputstring < 10^6

"""

# input_string = 'she'
# 
def isValidMorse(input_string, target_string):

    l = r = 0
    """
    "mo", 
     ^
    "11001110"
     ^
     1110
         ^
    """
    while l <= len(input_string) - 1:
        if input_string[l] == " ":
            continue
        # get the morse code for letter at L
        code = morse_binary[input_string[l]]

        # iterate through code and target
        for c in code:
            if c != target_string[r]:
                return False    
            r += 1
        l += 1

    return True


assert isValidMorse("morsecode", "110011100100000000001010111010000000") == True
assert isValidMorse("wordle", "0110111001000100010000" ) == False
assert isValidMorse("morse code", "110011100100000000001010111010000000") == True
# assert isValidMorse("excep38ioN", "00001001010000110111011101001111001110") == False




