a=20
b=2

def swapnum():
    global a
    global b
    temp = a
    a = b
    b = temp

print("Before swapping")
print("A:",a)
print("B:",b)
swapnum()
print("After Swapping")
print("A:",a)
print("B:",b)
