"""
English to Pig-Latin, Pig-Latin to english translator !!!!!!!!TESTING!!!!!!!!!!!!!!!!!!!
Author: Nolan T. (CS118 Fall Class)
Last Edited: 10/19/2022 Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22
Purpose: This program is designed to take the input of a sentence, and convert it to pig latin, and then convert it back to regular plain english, and detect it. And also allow it to remove special chars.
"""
while True:
    theInput = str(input('\n\nInput a sentence to be translated:\n')).lower()
    remove = theInput.replace('?', '').replace('.', '').replace(',', '').replace('~', '').replace('!', '').replace('#', '').replace('$', '').replace('%', '').replace("'", '').replace("+", "") # Allow the deletion of "," or "." or "?"
    trans = remove.split()
    if not theInput:
        exit()
    if "-yay" in remove or "-ay" in remove:  # Language Detector
        final=""
        ok = theInput.split()
        for words in ok:
            last = words[len(words)-3]
            final+=last
            for x in range(len(words)-3):
                final+=words[x]
            final+=" "
            bruh = str(final)
            hmm = bruh.replace("-", "").replace("yy", "y").replace("yare", "are") # Remove the "y" and "yay" and "yare" and "yy"
        print('\nTranslated into English:\n' + hmm)
    else:
        for secondary, words in enumerate(trans):
            if words[0] in 'aeiouy':
                trans[secondary] = trans[secondary] + "-yay"
            else:
                for third, char in enumerate(words):
                    if char in 'aeiouy':
                        trans[secondary] = words[third:] + "-" + words[:third] + "ay"
                        break
        print('\nTranslated into Pig-Latin:\n' + ' '.join(trans))