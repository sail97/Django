'''
a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a.count("b"))
a.remove("b")
print(a)
x = slice(0, 8, 2)
print(a[x])

'''

## remove all values of 2
'''
a = [2,2,2,1,4,5,6,7]

def remove_value(list, item):
    x = list.count(item)
    for i in range(x):
        list.remove(item)
    return list

print(remove_value(a,2))

# another method
while 2 in a:
    remove(2)
print(a)

'''

# ch = ['a','b','c','d','e']
# # for i in ch:
# #     print(i) 
# # for i in range(len(ch)):
# #     print(ch[i], i)
# print(ch[::])

a = int(input("enter no. of fruits: "))
fruits = []

for i in range(a,8):
    fruit = input("Enter the fruit: ")
    fruits.append(fruit)

print(fruits)