# # https://peps.python.org/pep-0008/ - style guide

# # Variables and Data types

# name = "neut"
# name_length = 4
# print(name)
# print(name_length)

# # # multiple var declaration in one line

# name, name_length = "neut", 4
# print(name)
# print(name_length)

# name_length = "4"
# print(type(name_length))
# name_length = int("4")
# print(type(name_length))

# # List

# name_list = ["neut", "247CTF", "asd"]
# print(type(name_list))

# name1, name2, name3 = name_list
# print(name1)
# print(name2)

# # Tuple

# name_tuple = ("neut", "247CTF")
# print(type(name_tuple))
# print(name_tuple)

# name_dictionary = {"neut":4, "247CTG":6}
# print(type(name_dictionary))
# print(name_dictionary)

# name_boolean = True # or False
# print(type(name_boolean))
# print(name_boolean)

# name_range = range(6)
# print(type(name_range))
# print(name_range)

# name_bytes = b"neut2"
# print(type(name_boolean))
# print(name_bytes)

# #Numbers

# t1_int = 1
# t1_float = 1.0
# print(t1_int)
# print(t1_float)
# print(type(t1_int))
# print(type(t1_float))

# #Complex numbers
# print("\n Complex numbers")

# t1_complex = 3.14j
# print(t1_complex)
# t1_hex = 0xa
# print(t1_hex)
# print(type(t1_hex))

# t1_octal = 0o10
# print(t1_octal)
# print(type(t1_octal))

# print(1+0x1+0o1) #3

# print(abs(4))
# print(abs(-4))

# print(round(8.4))
# print(round(8.5))
# print(round(8.6))

# print(bin(8)) #binary
# print(hex(8)) # hex

# # String formating

string1 = "I am a string"
string2 = "I am a string2"
print(string1)
print(string2)

string3= """I am a long
long
string3!"""
print(string3)

string4 = "I\" am a escaped string\n newline"
print(string4)

string5 ='I \' am string'
print(string5)

string6 = "I' am string"
print(string6)

string7 = "I\"m a string \n I\"m on a new line!"
print(string7)

string8 = "\\ \x41\x42\x43"
print(string8)    # \ ABC

string9 ='aaaaaaaaa'
print(string9)

string10 = "a"*10
print(string10)
print(len(string10))

print("string" in string4)
print("next" in string4)
print(string4.startswith("I"))
print(string4.index('string'))
print(string9.upper())
print(string9.lower())

messy_string = "            Messy String!       "
print(messy_string)
print(messy_string.strip())
print(messy_string.replace("!", "?"))
print(messy_string.replace("!", "?").strip())
print(messy_string.replace("String", "example").strip())
print(messy_string.split())

messy_string1 = "Messy,string!"
print(messy_string1.split(','))

string11 = "I am a string"
print(string11.encode())
print(string11.encode("UTF-8"))

print(string11.rjust(25))
print(string11.rjust(25,"x"))
print(string11.ljust(25))
print(string11.ljust(25,"x"))

# Strings are immutable

print("I am " +  "a string")
#print("string11 is " +len(string11) + " char long")  error:can only concatenate str (not "int") to str
print("string11 is " +str(len(string11)) + " chars long")

print("string11 is {} chars long!".format(len(string11)))
print("{} {} {}".format(len(string11), 5.0, 0x12))

#Placeholder
print("{length}".format(length=len(string11)))

length = len(string11)
print(f"string11 is {length} chars long")

print("string11 is {length} chars long".format(length = len(string11)))
#print("string11 is {length} chars long".format(length = .2f))

print("string11 is %d chars long!" % len(string11))
print("string11 is %f chars long!" % len(string11))
print("string11 is %x chars long!" % len(string11))

