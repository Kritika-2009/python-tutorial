import json
x = open("configuration.json", "r")
content = x.read()
# print (content)
data = json.loads(content)
# print (data)
# inquiry = input("What do you want to know:\n Hotel name \n Empty Rooms \n Single Bed \n Double Bed \n Food Options \n") 
# for z in data:
    # if inquiry == z:
        # print (data[z])
# if inquiry == "Hotel name":
count = 0
for z in data:
    print (f"Hotel Name : {data[z]}")
    break
for z in data:    
    if type(data[z]) == list:
        print (f"Total Rooms: {sum(data[z])}")
        break 
for z in data:
    if type(data[z]) == dict:
        for w in data[z]:
            # print (data[z][w])
            for q in data[z][w]:
                for e in q:
                    count += len(q[e])
print (f"Vacant Rooms: {count}")
y = 0
for z in data:
    if type(data[z]) == list:         
        y += 1
        if y == 2:
            print (f"Food Options: {data[z]}")



                    
            

        
