num= int(input("Enter a number:"))
s= num*num
sumof= 0
while s>0:
    sumof=sumof+s%10
    s= s//10
if (num == sumof):
    print("Neon Number")
else:
    print("Not a Neon Number")