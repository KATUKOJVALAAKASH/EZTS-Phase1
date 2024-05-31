n=int(input("Enter the year:"))
if(n<0 or n>9999):
    print("Invalid year")
elif(n%4==0 and (n%100!=0 or n%400==0)):
    print('Leap year')
else:
    print('Not a leap year')
