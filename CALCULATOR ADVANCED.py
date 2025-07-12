import re

regex = r"(\d+)"
regex_1 = r"(\W+)"
test_str = ""
lis = []
arr = []

def init():
  test_str = input()
  matches = re.finditer(regex, test_str, re.MULTILINE)
  
  for matchNum, match in enumerate(matches, start=1):
    print (match[0])
    dig = str(match)
    numb = dig.split(" ")[4].split("'")[1]
    fin_num = int(numb)
    lis.append(fin_num)


  matches_1 = re.finditer(regex_1, test_str, re.MULTILINE)
  for matchNm, match in enumerate(matches_1, start=1):
    print (matches)

init()


