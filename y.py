n=int(input())
p=0
for i in range(0,n,1):
    s=p+i
    print("Current Number",i,"Previous Number",p,"Sum:",s)
    p=i