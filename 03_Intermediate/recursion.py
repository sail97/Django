'''
function calling itself

base case
a smaller solution

'''

# add n number
'''
def sum_rec(n):
    if n == 1:
        return 1
    elif n <= 0:
        return "Null"
    else:
        return n + sum_rec(n-1)

print(sum_rec(0))
'''


'''
def fib(n):
    if n==0 or n ==1:
        return n
    return fib(n-1)+fib(n-2)

for i in range(6):
    print(fib(i),end=" ")


print(fib(5))

'''
'''
def power(a, b):
 
    if b == 0:  
        return 1
   
    return (a*power(a, b-1))

print(power(3,2))
'''