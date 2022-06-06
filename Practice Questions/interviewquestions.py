# replace spaces with nothing
'''
a = input("Enter a sentence : ")
b = ""
for str in a:
    if str != " ":
        b = b+str
print(b)

# another way
        
print(a.replace(""," "))

'''

# Print fibonnaci terms
'''
v = int(input("Enter a number : "))

def fibseries(n):
    if n == 0:
        print(0)
    if n == 1:
        print(0,end =",")
        print(1)
    if n>1:
        a = 0
        b = 1
        print(a,end=",")
        print(b,end=",")
        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
            print(c, end = ",")

# Print fibonnaci sum till n terms

def fibsum(n):
    if n == 0:
        print(n)
    if n == 1:
        print(n)
    else:
        sum = 0
        a = 0
        b = 1
        sum = a+b
        for i in range(2,n+1):
            c = a+b
            sum+=c
            a = b
            b = c
        print(sum)

fibsum(v)

'''

# Finding second largest number in an array

'''
number = []
n = int(input("No. of elements : "))
for i in range(0,n):
    ele = int(input("Enter the values for the array: "))
    number.append(ele)
number.sort()
print(number)

x = len(number)
fmx = max(number[0],number[1])
smx = min((number[0],number[1]))

for i in range(2,x):
    if number[i]>fmx:
        smx = fmx
        fmx = number[i]
    elif number[i]>smx and fmx != number[i]:
        smx = number[i]
print("Second largest number is : ",smx)

# another method
print("The second largest number is :", number[-2])

'''

# Fibonacci using Recursion

'''
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(15)) 

'''
# count no. of digits
'''
a = int(input("Enter a number: "))

count = 0
while a>0:
    rem = a%10
    count+=1
    a = a//10

print("No. of digits: ",count)

'''

# to find whether given no. is prime or not
'''
a = int(input("Enter a number : "))

if a>1:
    for i in range(2,a):
        if (a%i) == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("It is not a prime number")

'''
