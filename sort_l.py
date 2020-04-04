items = [["apple",  200, 38],
         ["kiwi",   130, 40],
         ["orange",  90, 20],
         ["grape",  380, 30],
         ["peach",  400, 10],
         ["cherry", 300,  5],
         ["banana",  80, 36],
         ["lemon",  150, 20]]

for i in range(len(items)):
    items[i].append(items[i][1] * items[i][2])

items.sort(key= lambda x:x[3], reverse = True)

for i in range(len(items)):
    print(items[i][0].ljust(10), str(items[i][1]).rjust(5), str(items[i][2]).rjust(5),str(items[i][3]).rjust(10))

