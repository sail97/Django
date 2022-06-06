# Q1) find greatest of 4 numbers
'''
number = []
n = int(input("How many values : "))

for i in range(1,n+1):
    num = int(input("enter the numbers : "))
    number.append(num)


print("The largest value is : ",max(number))

'''

# Q2) 
'''
m1 = int(input("Enter the marks of 1st subject : "))
m2 = int(input("Enter the marks of 2nd subject : "))
m3 = int(input("Enter the marks of 3rd subject : "))
total = 300
pass_marks = 300*(40/100)
fail_mark = 33
if (m1+m2+m3)>=pass_marks and (m1 or m2 or m3)>=fail_mark:
    print("The student has passed")
else:
    print("Sorry, the Sudent failed!")
'''


# Q3) detect spams
'''
sentence = input("enter a sentence: ")
spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subsribe this"
spam4 = "click this"
if sentence==(spam1):
    print("this is spam")
elif sentence==spam2:
    print("this is spam")
elif sentence==spam3:
    print("this is spam")
elif sentence==spam4:
    print("this is spam")
else:
    print("Not spam")
'''


# Q4) 
'''
username=input("Enter a name: ")
if len(username)<=10:
    print("it is less than 10 characters")
else:
    print("It is more than 10 characters")
'''

# Q5) given a name is in a list or not
'''
names=["viha","sam","harish","srikar","ayush","shreeya","gopi","yasha"]
name=input("Enter a name: ")
if name in names:
    print("is present")
else:
    print("not present")
'''
# Q6) calculate the grade
'''
mark = int(input("Enter the marks: "))
if mark in range(90,100):
    print("exemplary")
elif mark in range(80,90):
    print("A")
elif mark in range(70,80):
    print("B")
elif mark in range(60,70):
    print("C")
elif mark in range(50,60):
    print("D")
elif mark in range(0,50):
    print("F")
else:
    print("go Die!")
'''

# Q7)
# only taking if it upper but not lower 
'''
word = "Harry"
sentence = input("Enter a sentence: ")
if word in sentence:
    print("It is")
else:
    print("It is not")
'''