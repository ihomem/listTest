__author__ = 'irvin'

myMatrix = [[11,12,13],[21,22,23],[31,32,33]]

fruits =['avocados','bananas','oranges','grapes','mangos']

vegetables = ['carrots','potatoes','onions','leeks','celery']

inventory = ['shoes','socks','10 coins','spear','hammer','spanner','wood','books']

for i, value in enumerate(fruits):
    print(i, value)

######

for row in myMatrix:
    for i, value in enumerate(row):
        print(i, value,)
    print()

######

for fru, veg in zip(fruits, vegetables):
    if fru < veg:
        print(fru, "are better than", veg)
    else:
        print(veg, "are better than", fru)
