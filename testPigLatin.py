"""
English to Pig-Latin, Pig-Latin to english translator !!!!!!!!TESTING!!!!!!!!!!!!!!!!!!!
Author: Nolan T. (CS118 Fall Class)
Last Edited: 10/18/2022
Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22

This program is designed to take the input of a sentence, and convert it to pig latin, and then convert it back to regular plain english, and detect it.
"""

"""
s = input("Input text to be translated: ")
lst = s.split()
print(lst)

for word in lst:
    word += "-"
    if word[0] in "aeiouy":
        word+="yay"
        print(word)
"""

words = str(input("Input Sentence:")).split()

for word in words:
    #word += "-"
    if word[0] in "aeiouy":
        word += "yay"
        #print(word)
    print(word[1:] + word[0] + "ay", end=" ")
print()
