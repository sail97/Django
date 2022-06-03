# Q1) Program to store 7 fruits in a list

# fruits = []
# for i in range(0,7):
#     fruit = input("Enter the fruits: ")
#     fruits.append(fruit)
# print(fruits)

# Q2) Accept marks of 6 students and display them in sorted manner
'''
marks = []
for i in range(0,6):
    mark = input("Enter the score : ")
    marks.append(mark)

marks.sort()
print(marks)
'''

# Q3) tuple cannot be changed

'''
l = ['a','b','c','d']
t = ('a','b','c','d')
print(type(l))
print(type(t))
t[1] = 'z'
print(t[1])

'''

# Q4) sum of 4 numbers
'''
num = []
for i in range(0,4):
    n = int(input("Enter the numbers: "))
    num.append(n)
print(num)
sum_of_num = sum(num)
print("The sum of numbers is:{0}".format(sum_of_num))

'''

# Count the no. of zeros
'''
a = (7,0,8,0,0,9)
print(a.count(0))

'''