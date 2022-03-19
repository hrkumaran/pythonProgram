# Python3 program to add two numbers 

num1 = 15
print ( id(num1))

num1 = 17
print ( id(num1))
num2 = 12
num2=num1
print ( id(num1))
print ( id(num2))

# Adding two nos 
sum = num1 + num2 

# printing values 
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum)) 
print ( type(num1))
print ( id(num1))

a="try1 kumaran"
print(a[0:6])
print(a[:6])
print(id(a[0:6]))
print(id(a[:6]))
print(a[5:len(a)])
print(a[5:])
print(type(a))
print(len(a))

b="try2";
print(b)
c=a+b;
print(c)
d=2;
#e=c+d;
#print(type(e)) # fails
f=c+str(d)
print(f)