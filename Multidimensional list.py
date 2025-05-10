a = [
    [1,2,3,4,5,6,7,89,98],
    [2, 3 ]
]

#print (a)

for i in a:
    i.reverse()
    print(i)
    for x in i:
        print(x+2)