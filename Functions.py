print("TYPES OF FUNCTIONS:\n 1. Return & Arguments\n 2. Return\n 3. Arguments\n 4. Nothing")
print()
def Sum1(a,b):
    total=a+b
    return total    
def Sum2():
    a=int(input("Enter a Number:"))
    b=int(input("Enter a Number:"))
    total=a+b
    return total
def Sum3(a,b):
    print(a+b)
def Sum4():
    a=int(input("Enter a Number:"))
    b=int(input("Enter a Number:"))
    print(a+b)

print(Sum1(2,3))
print(Sum2())
Sum3(2,3)
Sum4()
