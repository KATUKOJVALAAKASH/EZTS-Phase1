def fact(n):
    if(n==0 or n==1):
        res=1
        return res;
    else:
        res=n*fact(n-1)
        return res
N=int(input("Enter any number:"))
print("The factorial of the given number is=",fact(N))