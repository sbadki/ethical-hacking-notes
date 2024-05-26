print(1)
    #print(2)
#f = open("abcdef")

try:
    f = open("abcdef")
except:
    print("The file doesn't exist!")

try:
    f = open("abcdef")
except Exception as e:
    print(e)
finally:
    print("This message")

print("----------------------------")
try:
    f = open("abcdef")
except FileNotFoundError as e:
    print("File doesn't exist!")
finally:
    print("This message!")


n = 100
if n == 0 : 
    raise Exception("'n' can't be 0!")
print(1/n)
