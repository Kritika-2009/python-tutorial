a = {"name" : ["Kritka", "Ayesha"], "Class" : 10, "Section" : "D"}
print(a)
print(a["name"])

for x in a:
    print (x)
    print (a[x], type(a[x]))
    if type(a[x]) == list:
        for j in (a[x]):
            print (j)
    else:
        print (a[x])
a.pop("Class")
print(a)
del a["Section"]
print(a)
a.clear() 
print(a)