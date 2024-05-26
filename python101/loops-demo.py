a = 1
while a < 5 :
    print(a)
    break

for i in [0,1,2,3,4]:
    print(i+6)

for i in range(5):
    print(i+2)

for i in range(5):
    for j in range(5):
        print(i,j)

print("-----------------")
for i in range(5):
    if i == 2 :
        break
    print(i)
        

for i in range(5):
    if i == 2 :
        continue
    print(i)
print("-----------------")    
for i in range(5):
    if i == 2 :
        pass
    print(i)
    
for c in "string" :
    print(c)

for key,value in {"a":1, "b":2, "c":3, "d":4}.items():
    print(key, value)


