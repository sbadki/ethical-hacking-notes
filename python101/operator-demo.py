# Boolean operator

valid = True
not_valid = False
print(valid == True)
print(not_valid == True)

print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print((10<9) == True)
print((10==10) == True)
print((10 != 10) == True)
print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 > 9) == True)

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)
print(bool(0))
print(bool(1))
print(bool(0) == False)
print(bool(1) == True)

x = 13
print(bin(x)) #0b1101
print(bin(x)[2:].rjust(4,"0")) #0b0100

y = 5 #0101
print(bin(y)[2:].rjust(4,"0"))
print("Bitwise & ")
print(bin(x & y)[2:].rjust(4,"0"))
print("Bitwise | ")
print(bin(x | y)[2:].rjust(4,"0"))

print(bin(x >> 1 )[2:].rjust(4,"0"))
print(bin(x >> 2 )[2:].rjust(4,"0"))
print(bin(x << 4 )[2:].rjust(4,"0"))

