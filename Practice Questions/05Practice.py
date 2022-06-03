# Q1) hindi dictionary with values of english translation

# hindi_dict = {"namaste": "Hello", "kaise ho":"how are you","kithab":"book","kursi":"chair"}
# for key output
# for i in hindi_dict.keys():
#     print(i)
# #for value output
# for i in hindi_dict.values():
#     print(i)
# print(hindi_dict["kithab"])
# a = input("Enter the word : ")
# print(hindi_dict[a])

# Q2) display all the 8 numbers and display all unique numbers
'''
a = []
for i in range(0,8):
    number = int(input("Enter the numbers : "))
    a.append(number)
print(set(a))

'''

# Q3) can we have int and string in the same set
'''
Yes it can have string and integer in the same set.
a = {18,"18"}
print(a)

'''

# Q4) 

'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

'''

# Q5) 

'''
s = {}
print(type(s))

'''

# Q6) 


n = 4
friends = dict(input("Enter the name and language : ").split() for _ in range(n))
print(friends)


# Q9)
'''
s = {8,7,12,1,2}
print(type(s))
'''
# no