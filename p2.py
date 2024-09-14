st=input("Enter a string : ")
st=st.upper()
for i in range(65,91):
    c=0
    for j in st:
        if chr(i)==j:
            c+=1
    if c!=0:
        print(f"Frequency of {chr(i)} = {c}")