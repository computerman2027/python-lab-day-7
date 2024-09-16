try:
    r1=int(input("Enter no of row of 1st matrix : "))
    c1=int(input("Enter no of column of 1st matrix : "))
    r2=int(input("Enter no of row of 2nd matrix : "))
    c2=int(input("Enter no of column of 2nd matrix : "))
    if(r1!=r2 or c1!=c2 or c1<=0 or r1<=0 or c2<=0 or r2<=0):
        print("Matrix size not proper. matrix cannot be added")
    else:
        m1=[]
        print("Enter numbers of 1st matrix : ")
        for i in range(r1):
            row=[]
            for j in range(c1):
                n=int(input())
                row.append(n)
            m1.append(row)
        m2=[]
        print("Enter numbers of 2nd matrix : ")
        for i in range(r2):
            row=[]
            for j in range(c2):
                n=int(input())
                row.append(n)
            m2.append(row)
        sum=[]
        for i in range(r1):
            rowsum=[]
            for j in range(c1):
                rowsum.append(m1[i][j]+m2[i][j])
            sum.append(rowsum)
        print("sum = \n")
        for i in range(r1):
            for j in range(c1):
                print(sum[i][j],"",end="\t")
            print()
except:
    print("Some error occured\n")