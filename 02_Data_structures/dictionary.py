# friends = dict(input("Enter name and age: ").split() for _ in range(4))
# print(friends)
'''
friends = {'sam': '27', 'chitti': '25', 'john': '34', 'viha': '23'}
friends['harish'] = 24
print(friends)
for k,v in friends.items():
    print(f"key is {k} and value is {v}")
'''
# count frequency of each character in a given string

# s = "we are learning"
# freq={}
# count = 0
# for i in s:
#     if freq.get(i):
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# given a pragraph, find the occurence of each word

# a=s.split()
# print(a)
# for i in a:
#     if freq.get(i):
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)


'''
def count_occurrences(str, word):
    a = str.split(" ")
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
            count = count + 1
    return count

print(count_occurrences(s, "are"))      
'''