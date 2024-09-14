passwoord = "abcdeffgjg"
length = len(passwoord)

if length < 6:
    print("Weak")
elif length <= 8:
    print("Medium")
else:
    print("Strong")