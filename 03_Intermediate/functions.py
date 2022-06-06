# paramterized function
'''
def profile(name,age):
    print(f"name is {name} and age is {age}")

profile("john",13)
'''
# default function
     # providing a default function
'''     
def profile(name,age="NA"):
    print(f"name is {name} and age is {age}")

profile("john")
'''
# keyword functions
'''
def profile(name="NA",age="NA"):
    print(f"name is {name} and age is {age}")

profile(age = 13,name = "John")

'''

# return statement
'''
def calc(num1,num2):
    return num1+num2,num1-num2

ans1,ans2 = calc(2,3)
print(f"sum is {ans1}")
print(f"diff is {ans2}")
'''

# variable length arguments
'''
def func(*args):
    # print(args)
    # print(type(args))
    sum = 0
    count = 0
    for i in args:
        sum+=i
        count+=1
    print(f'count is {count}')
    print(f'count is {sum}')

func(1,2,3,4,5)

'''

# variable length keyword arguments
'''
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} = {v}')
func(fname = "john", age = 13)
'''

# lambda functions
# variable_name = lambda parameters : expression

'''
isEven = lambda x : x%2==0
sum = lambda a,b : a+b
print(isEven(10))
print(sum(4,5))
'''

#square a number if greater than 0 otherwise return null
'''
sqr = lambda x : x**2 if x>0 else "NA"
print(sqr(2))
'''

#map
'''
num = [1,2,3,4,5]
sqr = list(map(lambda x : x**2,num))
print(sqr)
'''



# filter
'''
num = [1,2,3,4,5]
odd = list(filter(lambda x : x%2!=0,num))
print(odd)
'''

# reduce
