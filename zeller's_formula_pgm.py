K=int(input("enter the date:"))
M=int(input("enter the month number:"))
D=int(input("last two digits if the year:"))
C=int(input("first two digits if the year:"))
if(M==1):
    M=11
F=K+(13*M-1)//5+D+(D//4)+(C//4)-2*C
print("F=",F)
result=F%7
print(result)
if(result==1):
    print('sunday')
elif(result==2):
    print('monday')
elif(result==3):
    print('tuesday')
elif(result==4):
    print('wednesday')
elif(result==5):
    print('thursday')
elif(result==6):
    print('friday')
elif(result==7):
    print('saturday')