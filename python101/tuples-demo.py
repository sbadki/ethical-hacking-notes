tuple_items = ("item1","item2","item3")
print(type(tuple_items))
print(tuple_items)

tuple_numbers = (1,2,3)
print(type(tuple_numbers))
print(tuple_numbers)

tuple_repeat = ("Combined!,") * 4
print(tuple_repeat)
mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)

item1, item2, item3 = tuple_items
print(item1 + " : " + item2 + " : " +item3)

print("item3" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index(item2))
print(tuple_items[0])
print(len(tuple_items))
print(tuple_items[-1])
print(tuple_items[-2])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-1])
print(tuple_items[-3:-1])

string = "I am a string"
print(string[0:4])
print(string[-1])

