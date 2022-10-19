"""
English to Pig-Latin, Pig-Latin to english translator !!!!!!!!TESTING!!!!!!!!!!!!!!!!!!!
Author: Nolan T. (CS118 Fall Class)
Last Edited: 10/18/2022 Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22
Purpose: This program is designed to take the input of a sentence, and convert it to pig latin, and then convert it back to regular plain english, and detect it.
"""
theInput = input('Input a sentence to be translated to pig-latin: ').lower()
translationToPL = theInput.split()

for secondary, words in enumerate(translationToPL):
    if words[0] in 'aeiou':
        translationToPL[secondary] = translationToPL[secondary] + "-yay"
    else:
        vowel = False
        for third, char in enumerate(words):
            if char in 'aeiou':
                translationToPL[secondary] = words[third:] + "-" + words[:third] + "ay"
                has_vowel = True
                break

print('Translated to Pig-Latin:' + ' '.join(translationToPL))
