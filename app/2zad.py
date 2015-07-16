import math
def fill_tetrahedron(x):
    n=int(x)
    x=n**3
    n=x/((6*1000)*(2**0.5))
    return n
w=[]
n=input()
x=int(n)
#p=0
#c=0
b=0
while b<x:
    w.insert(b,int(input()))
    b=b+1
#print(w[0])
#print(fill_tetrahedron(w[2]))
water=int(input())
def tetrahedron_filled(w,water):
    p=0
    c=0
    while p<x:
        if fill_tetrahedron(w[p])<=water:
            c=c+1
        p=p+1
    return c
print(tetrahedron_filled(w,water))
#print(p)
