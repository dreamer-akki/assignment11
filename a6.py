# Write a python script to calculate factorial of a given number

n=int(input("Enter the Limit:"))
a=0
for i in range(1,n+1):
    a=a+i*1
print("factorial of ",n,"is:",a)