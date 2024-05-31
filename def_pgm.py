def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
def fact(n):
    if(n==0 or n==1):
        res=1
        return res;
    else:
        res=n*fact(n-1)
        return res
N=int(input("Enter any number:"))
print("The factorial of the given number is=",fact(N))
def palindrome(str):
    n=input('Enter the string')
if(str(n)==(str(n)[::-1])):
    print("It's palindrome")
else:
    print("Not a palindrome")
palindrome(str)
    
    

    

