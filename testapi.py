theInput = str(input('\n\nInput a sentence to be translated:\n')).lower()
remove = theInput.replace('?', '').replace('.', '').replace(',', '').replace('~', '').replace('!', '').replace('#',                                                                                                              '').replace('$', '').replace('%', '').replace("'", '').replace("+", "")  # Allow the deletion of "," or "." or "?"
sentence = remove.split(" ")
english = ""
for word in sentence:
    if word[:len(word) - 4:-1] == 'yaw':
        english += word[:len(word) - 3] + " "
    else:
        noay = word[:len(word) - 2]
        firstconsonants = noay.split("a")[-1]
        consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
        english += firstconsonants + consonantsremoved + " "