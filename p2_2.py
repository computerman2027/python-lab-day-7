st=input("Enter a string : ")
st=st.upper()
freq=[0]*26
for ch in st:
    if(ch>='A' and ch <='Z'):
        freq[ord(ch)-65]+=1
for i in range(26):
    if(freq[i]!=0):
        print(f"Frequency of {chr(i+65)} is {freq[i]}")