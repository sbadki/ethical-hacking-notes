list = ["A","B","C","D","E","F"]
print(list)

list2 = ["1", 1, 2.0, ["A","B"], [], ("A"), False]
print(list2)

print(list[0])
print(list[-1])
print(list2[3][0])
print(list2[3][-1])

list[0] = "X"
print(list)

#delete first element
del list[0]

list.insert(0, "A")
print(list)
list.append("G")

#Inbuilt runction - max, min, index, count, pop, extend, reverse, clear
 
list = list[::-1]
print(list)

list3 = [8,24,1,5,8]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

list4 = list3
list4[2] = "X"
# Modifying any list would affect both
print(list4)
print(list3)

# Copies only value
list5 = list4.copy()
list5[2] = "A"
print(list5)
print(list4)

list6= ["1","2","3"]
print(list6)

#[TODO- error]
#list7 = list(map(float, list6))
#print(list7)
