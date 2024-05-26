
# Does not read
# f = open('top-100.txt','r')
# print(f)


f = open('top-100.txt','r')
print(f.read())
print("-------------------")
print(f.readline())
print("-------------------")
# Already read 
print(f.readline())
# If u wish to ready then call seek
f.seek(0)
print(f.readline())

f.seek(0)
for line in f:
    print(line.strip())
f.close

f = open("test.txt", "w")
f.write("first line")
f.close

f.write("second line")
f.close()
print(f.name)
print(f.closed)
print(f.mode)

#for larger files - gives error
# with open('rockyou.txt') as f:
#     for line in f:
#         pass
print("----------------------")
#for larger files
with open('rockyou.txt', encoding='latin-1') as f:
    for line in f:
        pass
