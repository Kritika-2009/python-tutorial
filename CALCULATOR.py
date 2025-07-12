num1 = int(input("Enter the first number:\n"))
ops = input("Enter the operation: \n")
num2 = int(input("Enter the second number:\n"))
match ops:
    case "*":
        print (num1*num2)
    case "+":
        print (num1+num2)
    case "/": 
        print (num1/num2)
    case "-":
        print (num1-num2)
   
if ops != "*" and ops != "+" and ops != "-" and ops != "/":
    print ("VALUE ERROR")
    print ("INVALID OPERATION")