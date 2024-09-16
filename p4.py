a=list(range(10))
# a=[x for x in range(10)]
b=[]
c=[]

for i in a:
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)

print("Even numbers list =",b)
print("Odd numbers list =",c)