import string
import random
dict1={1:'Contains Uppercase Character',2:'Contains Lowercase Character',3:'Contains Number',4:'Contains Special characters(only @, #, - and $)'}
for key,value in dict1.items():
    print(key,value)
dict2={1:string.ascii_uppercase,2:string.ascii_lowercase,3:string.digits,4:'@#-$'}

n=int(input("Enter number of rules you want in your password: "))
if n==0:
    n=4
RuleNo=list(dict1.keys())
# print(RuleNo)
randomList=random.sample(RuleNo,n)
# print(randomList)
finalStr=""
for a in randomList:
    finalStr+=dict2[a]
length=int(input("Enter the length of password you want: "))
ansList=random.sample(finalStr,length)
ans="".join(ansList)
print(ans)
