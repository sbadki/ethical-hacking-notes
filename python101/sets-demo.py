# sets are unorders and doesn't allow duplicates

set1 = {"a","b","c"}
print(set1)
print(type(set1))

# print(set1[0]) -- cant do this
set2 = {"a","a","a"}
print(set2)
print(len(set2))

set3 ={"a", 0, True}
print(set3)

set4 = set(("b",0, True))
print(set4)
set5 = set(("b",1, False))
print(set5)

set1.add("d")
print(set1)
set3.update(set4)
print(set3)

list1 = ["a","b","c"]
set6 = {4, 5, 6}
set6.update(list1)
print(set6)

set7 = {4, 5, 6}
print(set6.union(set7))

# error- don't have 1 in a set
#set6.remove(1)
# remove 4
set6.remove(4) 
# remove 6
set6.discard(6)
print(set6)

set6.pop()
print(set6)