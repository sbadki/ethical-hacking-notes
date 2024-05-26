#https://github.com/SrivathsanNayak/ethical-hacking-notes/blob/main/Python101_TCMSec/Python101/README.md

# Basics

* Python interpreter

```python3
1+1
2

python2
1+1
2

print("Hello world!")
exit()
```
* Pwn a shell

```
python3 -c 'print("Hello world!")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

* How to run python script calculate-demo.py
```
#!/bin/python3
print(1+1)

chmod +x calculate-demo.py
python3 calculate-demo.py

```
* To call main function calculate-demo.py
```
#!/bin/python3
print(__name__)
if __name__=="__main__":
        print("Hello World!")
```

* Syntax

```
# syntax-demo.py
def test():
    print("testing")
string = "Hello"
number = 10

test()
print(string)
print(number)

x = 2 + 1 \
    + 3
print(x)

y = 1           +             1
print(y)
print(                y               )

```
