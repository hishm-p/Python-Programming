num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    limit=num2
else:
    limit=num1
for i in range(1,limit+1):
    if (num1 % i ==0) and (num2 % i==0):
        gcd=i
print("The GCD of",num1,"and",num2,"is:",gcd)         

        

