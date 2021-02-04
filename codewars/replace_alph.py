''' 
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''
# Set a list with the alphabet to have a base to compare
signs = [' ', '!', '"', '·', '·', '·', '$', "'", '%', '&', '/', '(', ')', '=', '?', '¿', '.', ',', ';', ':']
alphabet = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',]
alphabet_lenght = len(alphabet)
print(alphabet_lenght)

# Create a function that sort the input sentece, compare the string with the base to obtain the number for each letter.

def alphabet_position(sentence):
    print(sentence)

    sentence_lower = sentence.lower()
    take_out_spaces = sentence_lower.strip()
    sentence_without_spaces = take_out_spaces.replace(' ','')
    print(sentence_without_spaces)

    for char in sentence_without_spaces:
        for sign in signs:
            
            
            if char == sign:
                char = char.replace(char, '')
                char_list = []
                char_list = char_list.append(char)  
        
        
        print(char)

        # char_in_sentence = []
        # char_in_sentence = char_in_sentence.append(char)
        # print(char_in_sentence)


if __name__ == "__main__":
    sentence = "The sunset sets at twelve o' clock."
    alphabet_position(sentence)