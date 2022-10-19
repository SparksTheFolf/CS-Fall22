"""
English to Pig-Latin, Pig-Latin to english translator !!!!!!!!TESTING!!!!!!!!!!!!!!!!!!!
Author: Nolan T. (CS118 Fall Class)
Last Edited: 10/18/2022 Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22
Purpose: This program is designed to take the input of a sentence, and convert it to pig latin, and then convert it back to regular plain english, and detect it.
"""
while True:
    theInput = str(input('\n\nInput a sentence to be translated:\n')).lower()
    remove = theInput.replace('?', '')
    trans = remove.split()
    if not theInput:
        print("No string inputted, ending program.")
        break
    for secondary, words in enumerate(trans):
        if words[0] in 'aeiou':
            trans[secondary] = trans[secondary] + "-yay"
        else:
            for third, char in enumerate(words):
                if char in 'aeiou':
                    trans[secondary] = words[third:] + "-" + words[:third] + "ay"
                    break

    print('Translated to Pig-Latin: ' + ' '.join(trans))
