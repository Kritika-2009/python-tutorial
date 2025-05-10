l = ["Hi", "Bye!", "Hello", "hii"]
a = input("Enter file location")
b = input("Enter File name")
print (int('1'))
for x in range(len(l)):
    f2 = open(a + b +str(x)+".txt", 'a')
    f2.write(l[x])
    f2.close()

    f = open("log"+str(x)+".txt", 'r')
    s = f.read()
    print(s)
    f.close()


q = open("task.py", "a")
q.write("\n print('Hello')")
q.close()
q2 = open("filesystem.py" , "r")
w = q2.read
print (w)