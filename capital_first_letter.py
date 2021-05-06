print("enter_your_code")
ch=input()
for i in range(len(ch)):
    if i ==0:
        if ch[i]>='a' and ch[i]<='z':
            d=ord(ch[i])
            d=d-32
            d=chr(d)
    else:
        pass
print(d+ch[1:])
