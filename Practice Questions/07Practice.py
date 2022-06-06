# Q1) Multiplication table
'''
a = int(input("Enter a number: "))
for i in range(1,11):
    print(a,"x",i,"=",a*i)
'''

# Q2)

'''
l1 = ["Harry","Saham","Sachin","Rahul"]
for i in l1:
    if i[0]=="S":
        print("Hello,"+str(i))
'''

# Q3) 
'''
a = int(input("Enter a number: "))
i=1
while i<=10:
    print(a,'x',i,"=",a*i)
    i+=1
'''

# Q4) given no. is prime or not
'''
a = int(input("Enter a number: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,"It is not prime")
            break
    else:
        print("it is prime")
else:
    print("It is not prime")

'''

# Q5) sum of first n natural numbers
'''
n = int(input("Enter the numbers: "))
i=1
sum = 0
while i<=n:
    sum = sum+i
    i=i+1
print(f"sum of first {n} numbers is: {sum}")

'''


# Q6) 
'''
a = int(input("Enter the number: "))
fact = 1
if a==0 or a==1:
    print(f"The factorial of {a} is 1")
for i in range(1,a+1):
    fact=fact*i
print(f"the factorial of {a} is {fact}")
'''

# Q10) 
'''
n=int(input("Enter a number : "))
for i in range(10,0,-1):
    print(n,'x',i,'=',n*i)

'''