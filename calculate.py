import re

arr = ["-", "+", "*", "/"]
regex = r"(\d+)"
regex_1 = r"(\W+)"
test_str = "1452+54784"

matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
	digit = "Match {matchNum} was found at {start}-{end}:{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
	dig = digit.split(" ")
	print (type(dig))
	for w in dig:
		print(w)

	
	   
    
matches_1 = re.finditer(regex_1, test_str, re.MULTILINE)
for matchNm, match in enumerate(matches_1, start=1):
    
    ops = "Match {matchNm} was found at {start}-{end}: {match}".format(matchNm = matchNm, start = match.start(), end = match.end(), match = match.group())
    for x in ops:
        print (x)
        if x == "*" or x == "+" or x == "-" or x == "/":
            print (x)

    
    
    
    
    
