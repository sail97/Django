# num = [1,2,3,4,5,6]
# nums = [i for i in range(0,7)]
# print(nums)

# even = [ i for i in range(0,11,2)]

#or

# even = [ i for i in range(0,11) if i%2==0]

# give a list, if a no is even provide its square or its cube

# l = [i**2 if i%2==0 else i**3 for i in range(0,11)]
# print(l)


# twoDMatrix = [[10,20,30],
#                 [40,50,60],
#                 [70,80,90]]

# l = len(twoDMatrix)
# print([[i[j]for i in twoDMatrix] for j in range(l)])

# mat = [[j for j in range(5)] for i in range(3)]
# print(mat)


# dictionary comprehension
'''
num = {i:i**2 for i in range(5)}
print(num)

val = {i.upper():i for i in "python"}
print(val)

'''
'''
keys = ['a','b','c','d']
vals = [1,2,3,4]
print({k:v for (k,v) in zip(keys,vals)})
'''

# generate a list which is divisible by 2 and 5

# nums = [i for i in range(100) if i%2 == 0 and i%5 == 0]
# print(nums)

