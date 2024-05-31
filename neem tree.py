#square box garden border rows are neem trees and middle are mange trees....
size=int(input("Enter the size of garden:"))
boxnum=int(input("Enter the of box number:"))
if(boxnum>0 and  boxnum<=size*size):
    if(boxnum>0 and boxnum<=size):
        print("Neem tree")
    elif(boxnum%size==0):
        print("Neem tree")
    elif(boxnum-1%size==0):
        print("Neem tree")
    elif(boxnum>(size*2)-1 and boxnum<=size**2):
        print("Neem tree")
    else:
            print("Mango tree")
else:
    print("Invalid box number")
    
        
    
    
    
 