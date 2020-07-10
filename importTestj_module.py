# i. this is a module.
# 1) This can be the main program.
# 2) It's also possible that some other module is the main program and it imports this module.

print("this is importTestj_module.py... __name__:",__name__)

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")