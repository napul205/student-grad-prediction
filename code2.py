num="10000"
def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    else:
        n=len(str(x))
        half=int(n/2)
        a=int (x/10**half)  
        b=int (x%10**half)
        c=int (y/10**half)
        d=int (y%10**half)
        ac=karatsuba(a,c)
        bd=karatsuba(b,d)
        ad_bc=karatsuba(a+b,c+d)-ac-bd
        return (ac*(10**(2*half))+(ad_bc*(10**half)))+bd

p=0
for i in range(len(num)):
    p=p*10+(int(num[i]))

print(p)
ans=karatsuba(p,p)
print(ans)