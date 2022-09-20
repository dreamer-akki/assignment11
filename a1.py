# 1. Write a python script to calculate sum of first N natural numbers.


n=int(input("Enter the Limit:\n"))
x=0
for i in range(1,n+1):
     x = x+i
    
print("sum of first",n,"numbers are: ",x)