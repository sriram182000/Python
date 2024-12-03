import sys

def add(a,b):
    res=a+b
    return res
def sub(a,b):
    res=a-b
    return res

num1=int(sys.argv[1])
operation=sys.argv[2]
num2=int(sys.argv[3])

if operation == "add":
    res=add(num1,num2)
    print(res)
else :
    res=sub(num1,num2)
    print(res)
