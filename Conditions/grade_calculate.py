score = 90

if score < 0 or score > 100:
    print("Invaliid Grade")
    exit()
elif score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")