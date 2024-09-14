num = 70

if num < 2:
    print("False")

else:
    for i in range(2,(int(num/2)+1)):
        if(num % 2 == 0):
            print("False")
            break
        else:
            print("True")