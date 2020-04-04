items = [["apple",  200, 38],
         ["kiwi",   130, 40],
         ["orange",  90, 20],
         ["grape",  380, 30],
         ["peach",  400, 10],
         ["cherry", 300,  5],
         ["banana",  80, 36],
         ["lemon",  150, 20]]

sales = \
    {'kiwi': (130, 40), 'grape': (380, 30), 'apple': (200, 38), "banana" : (80, 36),
     'peach': (400, 10), 'cherry': (300, 5), 'orange': (90, 25), 'lemon': (160,20)}

list_sale = [[key,sales[key][0], sales[key][1]] for key in sales.keys()]
items.sort()
list_sale.sort()

print(items)
print(list_sale)

for i in range(len(items)):
    if items[i] != list_sale[i]:
        print(items[i][0])