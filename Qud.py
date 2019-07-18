import math
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b*b-4*a*c
if d==0:
    x1=-b/(2*a)
    x2=x1
    print("the ans is {}{}".format(x1,x2))
elif d>0:
    x1=(-b+(math.sqrt(d)))/(2*a)
    x2=(-b-(math.sqrt(d)))/(2*a)
    print(x1)
    print(x2)
    print("the ans is {}{}".format(x1,x2))
else:
    rp=-b/(2*a)
    ip=float(math.sqrt(abs(d)))/(2*a)
    print("the ans is {}+{}i".format(rp,ip))
    print("the ans is {}-{}i".format(rp,ip))   


