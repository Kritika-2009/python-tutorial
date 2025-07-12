import re

regex = r"(\d+)"
regex_1 = r"(\W+)"
test_str = ""
lis = []
arr = []


test_str = "25+25"
matches = re.finditer(regex, test_str, re.MULTILINE)
matches_1 = re.finditer(regex_1, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
  digi = (match [0])
  lis.append(digi)
for matchNm, match in enumerate(matches_1, start=1):
  dig = (match[0])
  arr.append(dig)
  for w in lis:
    match arr:
      case "+":
        print (sum(lis))
      case "*":
        print (w*w)
      case "/":
        print (w/w)
      case "-":
        print (w-w)
  



lis = ["25","25","6","5"]
arr = ["+", "-", "*", "/"]
match arr:
  case "+":
    print (sum(lis))
  case "*":
    print (w*w)
  case "/":
    print (w/w)
  case "-":
    print (w-w)

  
zsx = input ()
match zsx:
  case "T":
    print("TUES")
  case "W":
    print("WEDNES")



    
