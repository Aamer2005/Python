
def fun():
    print("hello")
    exit()
    print("world")

print("start")
fun()
print("end")

import sys
def fun():
    print("hello")
    sys.exit()
    print("world")

print("start")
fun()
print("end")