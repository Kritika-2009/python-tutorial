l = ["A", "B", "C", "D", "E", "F", "G"]
w = [1,2,3,4,5]
s = len(w)
def abc(x, y):
    for z in l:
        print(f"{z} ABCD{x, y}")
    global s
    s += 1
    print(s)
    if s <= 7:
        print("sss")
        abc (l,w)    
abc(l, w)

for i in range(2):
    abc(65, 13)
