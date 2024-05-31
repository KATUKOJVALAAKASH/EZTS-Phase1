n=int(input("Enter the number:"))
def harmonic(n):
    if(n==1):
        return 1
    else:
        return(1/n)*pow(2,n)
print(harmonic(n))