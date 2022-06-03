# TODO : Grading System ( A, B, C, D, F)
#        Feedback System(1-5) 
     
'''
a = int(input("Enter the marks of the student : "))

def grades(score):
    if score>=90 and score<=100:
        print(" The grade is A")
        print("Rating = 5")
    elif score>=80 and score<=89:
        print("The grade is B")
        print("Rating = 4")
    elif score>=70 and score<=79:
        print("The grade is C")
        print("Rating = 3")
    elif score>=60 and score<=69:
        print("The grade is D")
        print("Rating = 2")
    else:
        if score>100:
            print("undefined score, not possible to get")
        elif score<60:
            print("Student Failed")
            print("Rating = 1")

grades(a)

''' 

# TODO : Check whether a given no. is odd or even

'''
a = int(input("Enter a number : "))

if a%2==0:
    print("no. is even")
else:
    print("no. is odd")

'''

# TODO : Greatest number among 4 digits     

# if user gives the input
'''
number = []
n = int(input("How many values : "))

for i in range(1,n+1):
    num = int(input("enter the numbers : "))
    number.append(num)


print("The largest value is : ",max(number))

'''
#if predifined

'''
n1 = 45
n2 = 105
n3 = 57
n4 = 99

if n1>n2:
    if n1>n3:
        if n1>n4:
            print(n1)
        else:
            print(n4)
    else:
        if n3>n4:
            print(n3)
        else:
            print(n4)
else:
    if n2>n3:
        if n2>n4:
            print(n2)
        else:
            print(n4)

'''