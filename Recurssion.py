# Recurssion function
count = 0

def abc(x,y):
    global count
    count -= 1
    print(count*x*y , " -~-~-~-~-~-~- ")
    if(count >= -1):
        print("1111")
        abc(0,1)
abc(5,9)
