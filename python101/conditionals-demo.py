if True:
    print(True)
if False:
    print(False)

if not False:
    print("Not False")

if 1 < 1 :
    print("1 < 1")
elif 1 >= 1:
    print ("1 <= 1")
else:
    print("else")

if 1 > 0 and 0 < 1 :
    print("1 > 0 and 0 < 1")

if 1 < 0 and 0 > 0 :
    print("1 < 0 and 0 > 1")

if 1 < 0 or 0 < 1 :
    print("1 <0 or 0 < 1")

if (1 < 0 or 0 < 1) and 1 == 1:
    print("1 < 0 or 0 < 1")

if (1 < 0 or 0 < 1) or 1 == 1:
    print("1 < 0 or 0 < 1")
