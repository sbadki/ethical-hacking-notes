test = input()
print(test)

test = input("Enter the ip:")
print(test)

while True:
    test = input("Enter the ip:")
    print(">>> {}".format(test))

    if test == "exit":
        break
    else:
        print("Exploiting")