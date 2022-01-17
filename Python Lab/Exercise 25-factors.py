def factor(num):
    print("The Factors of",num,"are:",end=" ")
    for i in range(1,num+1):
        if(num%i == 0):
            print(i,end=" ")

num=int(input("Enter a number to find it's factors:"))
factor(num)