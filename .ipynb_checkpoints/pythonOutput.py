word = "Python"
x = 0

'''

while x < len(word):
    print(word[x])
    x += 1
'''

for k in range(len(word)):
    for i in range(k+1):
        print(word[i], end='')
    print('\n')



#print(word[0])

