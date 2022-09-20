# Write a python script to calculate sum of digits of a given number


n=int(input("Enter a number:"))
dig=0
while n>0:
    rem=n % 10
    dig=dig+rem
    n=n//10
    
print("The sum of digits :",dig)