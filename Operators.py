a=int(input("Enter an Number:"))
b=int(input("Enter an Number:"))
print()
print("UNARY OPERATORS")
print("Binary Complement:",~a)
print("Negative:",-a)
print("Double Negative:",-(-a))
print()
print("ARITHMETHIC OPERATORS")
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
print("Exponent:",a**b)
print("Integer Division:",a//b)
print()
print("RELATIONAL OPERATORS")
print("Check Equal:",a==b)
print("Check Not Equal:",a!=b)
print("Greater Than:",a>b)
print("Lesser Than:",a<b)
print("Equal or Greater Than:",a>=b)
print("Equal or Lesser Than:",a<=b)
print()
print("LOGICAL OPERATORS")
print("And:",a>b and b>a)
print("Or:",a>b or b>a)
print("Not:",not(a>b))
print()
print("BITWISE OPERATORS")
print("&:",a>b & b>a)
print("|:",a>b | b>a)
print("^:",a>b ^ b>a)
print("Left Increment:",a>>1)
print("Right Increment:",b<<1)
print()
MyList =(a,b)
print("MEMBERSHIP OPERATORS")
print("In:",a in MyList)
print("Not In:",a not in MyList)
print()
print("IDENTITY OPERATORS")
print("Is:",type(a) is int)
print("Is Not:",type(a) is not float)
