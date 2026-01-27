#Program of Reverse number: 


rev=0   #initially keeping zero
n=int(input("Enter a number: "))  #taking input from user
org=n             #keeping a copy of user input to show before after in output
while n>0:        # loop will work till n>0
    d=n%10        #extract last digit of any number
    rev=rev*10+d  #keep adding last digit 
    n//=10        #remove last digit 
print(f"Original number: {org} , Reversed: {rev}")
