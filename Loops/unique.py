myList = [1,2,3,4]

unique_item = set()

for item in myList:
    if item in unique_item:
        print("Duplicate",item)
        break
    else: 
        unique_item.add(item)