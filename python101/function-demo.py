def function1():
    print("Hello from function1")
function1()
function1()

def function2():
    return "Hello from function2!"
function2()

print("--------------------------")
return_from_funtion2 = function2()
print(return_from_funtion2)

def function3(s):
    print("It {}".format(s))
function3("is")

def function4(s1, s2):
    print("{} {}".format(s1,s2))

function4("Hello","World!")

function4(s1="thing", s2="any")
function4(s2="any", s1="thing")

def function5(s1 = "default"):
    print("{}".format(s1))
function5()
function5("anything")

def function6(s1, * more):
    print("{}{}".format(s1, "".join([s for s in more])))
function6("hello")
function6("hello", "a")
function6("hello","a","b","c")

def function7(** ks):   # Dictionary
    for i in ks:
        print(i, ks[i])
    
function7(a="1", b="2", c="3")
function7(a="1", b="2", c="3", d="4")

def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))
    print(s,f,i,l)

function8("hello", 1.0, 2, ['A','B','C','D'])

v = 100
print(v)

def function9():
    v = 5
    v += 1
    print(v)
print(v)
function9()

def function9():
    #v += 1    # Error
    global v
    v += 1
    print(v)
print(v)
function9()

def function10():
    print("hello from function10")
def function11():
    function10()
    print("Hello from function11")
function11()

def function12(x):
    print(x)        # Recurssion
    # Fix, we need to put following if condition otherwise it be recursive call
    if x > 0:
        function12(x-1)
function12(5)

def function13(x):
    while x >= 0:
        print(x)
        x -= 1
function13(5)