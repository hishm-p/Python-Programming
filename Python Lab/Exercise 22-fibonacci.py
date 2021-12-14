def fibonacci(lim):
    a=0
    b=1
    if(lim == 0):
        print("Invalid Entry!")
    elif(lim == 1):
        print(a)
    else:
        print("The Fibonacci series of",lim,"terms is:")
        print(a,b,end=" ")
        for i in range(2,lim):
            c=a+b
            print(c,end=" ")
            a=b
            b=c

lim=int(input("Enter the no.of terms to be displayed: "))
fibonacci(lim)


