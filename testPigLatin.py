"""
English to Pig-Latin, Pig-Latin to english translator !!!!!!!!TESTING!!!!!!!!!!!!!!!!!!!
Author: Nolan T. (CS118 Fall Class)
Last Edited: 10/18/2022
Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22

This program is designed to take the input of a sentence, and convert it to pig latin, and then convert it back to regular plain english, and detect it.
"""
sentence = input('Enter a Sentence: ').lower()
words = sentence.split()

for i, word in enumerate(words):
    if word[0] in 'aeiou':
        words[i] = words[i] + "-yay"
    else:
        vowel = False
        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break
        if not vowel:
            words[i] = words[i] + "ay"

print(' '.join(words))
