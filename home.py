a=input()
b=len(a)
s=0
k=0
for i in range(len(a)):
    b=a[i]
    c=ord(b)
    if   'A'<= b<= 'Z':
        s+=1
    elif  'a'<= b<= 'z' :
        k+=1
print(s, k)
