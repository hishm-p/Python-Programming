def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact    

num=int(input("Enter a Number to find it's factorial: "))
fact=factorial(num)
print("The Factorial of",num,"is:",fact)
        
        
        
        
