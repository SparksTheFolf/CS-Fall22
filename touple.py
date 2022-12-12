model = ['14', '14 plus', '14 pro', '14 pro max']
memory = ['64', '128', '256', '512', '1024']
color = ['blue', 'purple', 'red', 'midnight', 'starlight', 'silver', 'gold', 'green']
price = ['699', '749', '999', '1099', '1199', '1299', '1399', '1499']

for x in model:
    for y in memory:
        for z in color:
            for t in price:
                print(x, y, z, t)
lst = [(x,y,z,t) for x in model for y in memory for z in color for t in price]
print(len(lst))
print(lst)

with open('sq.txt', 'w') as f:
    for i in lst:
        f.append(len(i));