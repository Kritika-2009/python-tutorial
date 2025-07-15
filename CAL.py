import re

lis = []
arr = []
test_str = input()


regex = r"\d+"
matches = re.finditer(regex, test_str)
for matchNum, match in enumerate(matches, start=1):
    
	dig = "Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
	initial = dig.split()
	lis.append(initial[6])
#print (lis)


regex = r"\W+"
matches = re.finditer(regex, test_str)
for matchNum, match in enumerate(matches, start=1):   

	ops = "Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
	intro = ops.split()
	arr.append(intro[6])
#print (arr)





for op in arr:
	match op:
		case "+":
			plus = arr.index(op)
			add = int(lis[plus]) + int(lis[plus+1])
                        
                                
    	    
		case "-":
			minus = arr.index(op)
			try:
				sub = add - int(lis[minus+1])
			except:
				sub = int(lis[minus]) - int(lis[minus+1])


		case "*":
			mult = arr.index(op)
			try:
				prod = sub * int(lis[mult+1])
			except:
				prod = int(lis[mult]) * int(lis[mult+1])

			
		case "/":
			div = arr.index(op)
			try:
				print(prod / int(lis[div+1]))
			except:
				print(int(lis[div]) / int(lis[div+1]))