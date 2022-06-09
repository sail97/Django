'''

try:
    pass

except:
    pass



'''
'''
n1=4
n2=0
try:
    #print(n1/n2)
    print(a)

except ZeroDivisionError as e:
    print(e)
    print("Demoninator cannot be zero")
except BaseException as e:
    print(e)

else:
    print("Either except block executes or else block gets executed")
finally:
    print("No matter what exception will occur it will get executed")

'''

# a=0
# if a==0:
#     raise "denominator can't be zero"

