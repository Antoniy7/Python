def ceaser_encrypt(str,n):
    m=len(str)
    p=0
    str=list(str)
    while p<m:
        if (str[p].isalpha):
            if str[p]=='Z':
                str[p]=chr(64)
            if str[p]=='z':
                str[p]=chr(96)
            str[p]=chr(ord(str[p])+n)
        p=p+1
    return str
x=input()
num=input()
num=int(num)
print(ceaser_encrypt(x,num))
