# Write a python script to calculate sum of squares of first N natural numbers

n=int(input("Enter the Limit:"))
a=0
for i in range(1,n+1):
    a=a+(i*i)
    
print("Sum of squares:",a)