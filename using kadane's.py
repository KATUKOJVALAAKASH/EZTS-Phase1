list=list(map(int,input().split()))
curr_max=list[0]
res=list[0]
for i in range(1,len(list)):
    if(list[i]>curr_max):
        curr_max=list[i]
        res+=curr_max
print(res)