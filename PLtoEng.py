theInput = str(input('\n\nInput a sentence to be translated:\n')).lower()
remove = theInput.replace('?', '').replace('.', '').replace(',', '')  # Allow the deletion of "," or "." or "?"
trans = remove.split()

english = ''

while True:
    for word in trans:
        if word[:len(word) - 4:-1] == trans:
            english += word[:len(word) - 3] + " "
        else:
            index = -3
            for letter in reversed(word[:-3]):
                if letter != 'a':
                    index -= 1
                else:
                    break
            english += word[index:-2] + word[:index - 1] + " "
    print(english)
    break