import os

def test():
   print("hello")

print("welcome to test Environment")
for i in range(0, 10):
    print(i)
print(os.getenv("PYTHON_VERSION"))
test()
