# Write a python script to calculate sum of first N odd natural numbers

n=int(input("Enter the Limit:"))
x=0
for i in range(1,n+1):
    if i%2!=0:
        print(i)
        x=x+i
print("Sum of fisrt",n,"odd natural numbers are:",x)    
