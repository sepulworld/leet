import pytest
import string

def uniqueMorseRepresentations(words):
    morse_alphabet = [ ".-","-...","-.-.","-..",".","..-.",
    "--.","....","..",".---","-.-",".-..","--","-.","---",
    ".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.." ]
    morse_code_transforms = set()
    
    for word in words:
        transform = ""
        for letter in word:
            letter_index = string.ascii_lowercase.index(letter)
            transform += morse_alphabet[letter_index]
        morse_code_transforms.add(transform)
    
    return len(morse_code_transforms)

assert uniqueMorseRepresentations(["gin", "zen", "gig", "msg", "mig", "rock", "buck", "tony"]) == 6