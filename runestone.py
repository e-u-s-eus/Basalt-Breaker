import sys

# Basalt Breaker by eus#0103

# Quickly checks a ciphertext against a number of keywords in a Vigenere cipher and gives a list of all Ceasar cipher
# shifts. Can be fed multiple alphabets/keys through input files.
# Part of the Vigenere/Caesar code was taken from:
# https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4?permalink_comment_id=4035102#gistcomment-4035102
# Run like: >python runestone.py <ciphertext> <keys file> <alphabets file>
# Example: >python runestone.py Y1ULZ0VUL keys.txt alphabets.txt
# Made for the Runestone Hunters Discord

# TODO:
# - Figure out how space is generally included in an alphabet (what position)
# - Add the option to either skip space or decode space like a character
# - Fix a BUNCH of edge cases


# Decrypts a Vigenere cipher using the ciphertext, the key and the alphabet
def vigenere(ciphertext, key, alphabet):
    result = ''
    for i in range(len(ciphertext)):
        letter_n = alphabet.index(ciphertext[i])
        key_n = alphabet.index(key[i % len(key)])
        value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]
    return result


# Decrypts a Caesar cipher using the ciphertext, the shift and the alphabet
def caesar(ciphertext, shift, alphabet):
    result = ''
    for i in range(len(ciphertext)):
        letter_n = alphabet.index(ciphertext[i])
        value = (letter_n - shift) % len(alphabet)

        result += alphabet[value]
    return result


# Reads a file
def read_file(filename):
    # Opening the file
    file = open(filename, 'r')
    # Reading the files
    read = file.read()
    # Putting them into lists
    split = read.split('\n')
    return split


# Returns an error if arguments are incorrect
if len(sys.argv) != 4:
    print('Invalid input: Incorrect arguments')
    exit()

# Sets ciphertext, keys and alphabets
text = sys.argv[1]
keys = read_file(sys.argv[2])
alphabets = read_file(sys.argv[3])

# Checks for every key if all of it's characters are contained in at least one alphabet
# Removes alphabets which don't contain any of the characters of key
for key in keys:
    for character in key:
        for alphabet in alphabets:
            if character not in alphabet:
                alphabets.remove(alphabet)

# Exits if a key doesn't match any alphabets
if not alphabets:
    print("Invalid input: One or more keys don't match any alphabets")
    exit()

# Checks for the ciphertext if all of it's characters are contained in at least one alphabet
# Removes alphabets which don't contain any of the characters of key
for character in text:
    for alphabet in alphabets:
        if character not in alphabet:
            alphabets.remove(alphabet)

# Exits if the ciphertext doesn't match any alphabets
if not alphabets:
    print("Invalid input: Ciphertext doesn't match any alphabets")
    exit()

# Computes the Vigenere Cipher and Caesar Ciphers for all matching alphabets
for alphabet in alphabets:
    # Prints alphabet
    print("ALPHABET: '" + str(alphabet) + "'\n")

    # Prints Vigenere outputs
    print('VIGENERE')
    for key in keys:
        print(key + ':\t' + vigenere(text, key, alphabet))

    # Prints Caesar outputs
    print('\nCAESAR')
    for i in range(1, 26):
        print(u'\u2191' + str(i) + u' \u2193' + str(abs(i - 26)) + '\t' + caesar(text, i, alphabet))

    print('\n')
