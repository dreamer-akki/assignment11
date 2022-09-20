# Write a python script to calculate sum of cubes of first N natural numbers

n=int(input("Enter a Limit:"))
a=0
for i in range(1,n+1):
    a=a+(i*i*i)
print("Sum of fisrt",n,"cubes:",a)