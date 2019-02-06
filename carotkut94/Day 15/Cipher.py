# Ceaser Cipher encryption
# Author Sidhant Rajora


# first approach is to generate the new letter with the shift of provided key
# and then join all the letters using join.

# it takes O(n) time and O(n) space

def encryptor(string, key):
    newLetters = []
    clampedKey = key % 26
    for letter in string:
        newLetters.append(getShiftedLetter(letter, clampedKey))
    return "".join(newLetters)


def getShiftedLetter(letter, key):
    newLetterCode = ord(letter)+key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96+newLetterCode % 122)


print(encryptor("xyz", 2))


"""
Second approach it to store the alphabets in a list and add the key to index and return the character on the 
new index.
"""


def getLetter(l, clampedKey, alpha):
    newLetter = alpha.index(l)+clampedKey
    return alpha[newLetter] if newLetter <= 25 else alpha[-1 + newLetter % 25]


def indexencryptor(string, key):
    newLetters = []
    clampedKey = key % 26
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for l in string:
        newLetters.append(getLetter(l, clampedKey, alpha))
    return "".join(newLetters)


print(indexencryptor("xyz", 2))
