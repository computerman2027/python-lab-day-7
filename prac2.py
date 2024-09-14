v=[]
print("Enter 10 no")
for i in range(10):
    nv=int(input(str(i+1)+" "))
    v+=[nv]
print("Creating histogram from values")
#print("elem","v","histo")
for i in range(len(v)):
        print(i,v[i],"*"*v[i])
