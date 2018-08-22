#Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input
#and that returns the missing letter in the array.
#You will always get an valid array. And it will be always exactly one letter be missing.
#The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:
#['a','b','c','d','f'] -> 'e'
#['O','Q','R','S'] -> 'P'

#(Use the English alphabet with 26 letters!)
alphabet = "abcdefghijklmnopqrstuvwxyz"
list = []
full = []
count = 0
list.append(tuple(letter for letter in alphabet))

def find_missing_letter(chars):
    for x in chars:
        for letter in alphabet:
            if letter == x.lower():
                full.append(x)
    return(full)

find_missing_letter(['a','b','c','e','f'])
