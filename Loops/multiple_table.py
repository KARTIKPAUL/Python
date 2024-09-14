number = 2
myList = []
for i in range(1,11):
    if(i == 5):
        continue
    else:
        myList.append(i*number)

print(myList)
