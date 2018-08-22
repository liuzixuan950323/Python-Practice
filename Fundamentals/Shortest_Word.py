#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

def find_short(s):
    l = min(len(words) for words in s.split())
    print(l)
    return l # l: shortest word length

s = input("Please enter your string: ")
find_short(s)
