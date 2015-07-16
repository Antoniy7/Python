import math
def  fill_tetrahedron(x):
    n=int(x)
    x=n**3
    n=x/((6*1000)*(2**0.5))
    return n


n=input()
print("%.2f" % fill_tetrahedron(n))
