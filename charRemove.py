while True:
    theInput = str(input('\n\nInput a sentence to be translated:\n')).lower()
    remove = theInput.replace('?', '').replace('.', '').replace(',', '')
    print(remove)