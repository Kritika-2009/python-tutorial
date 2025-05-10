import json

a = open("abcd.json" , "r")
x = a.read()

data = json.loads(x)
# print (data[1])
q = data[0]
for z in q:
    w = (q[z])
    if type(w) == list:
        print (w[0])
        d = w[0]
        for c in d:
            print (c, d[c])
            # print()
    