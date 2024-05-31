x=int(input("Enter the Number:"))
y=int(input("Enter the Number:"))
def lcm(x,y):
    z=x%y
    if(z==0):
        return x
    return x*lcm(y,z)/z
print(lcm(x,y))