items = [["apple",  200, 38],
         ["kiwi",   130, 40],
         ["orange",  90, 20],
         ["grape",  380, 30],
         ["peach",  400, 10],
         ["cherry", 300,  5],
         ["banana",  80, 36],
         ["lemon",  150, 20]]

sale = {}
for i in range(len(items)):
    sale[items[i][0]] = int(items[i][1]*items[i][2]*1.08)

for i in sale.keys():
    print(i.ljust(10),str(sale[i]).rjust(7))