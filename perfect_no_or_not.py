n=int(input("Enter your number:"))
count=0
for i in range(1,n):
    if(n%i==0):
        count=count+i
if(n==count):
    print("perfect number")
else:
    print("not a perfect number")