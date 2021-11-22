num=int(input("Enter a number to find it's Reverse:-"))
og=num
rev=0
while og>0:
    rem=og%10
    rev=rev*10+rem
    og=og//10
print("The Reverse of",num,"is:- ",rev)
