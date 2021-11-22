num=int(input("Enter a number to check whether it is armstrong or not:-"))
og=num
sum=0
while og>0:
    rem=og%10
    sum=sum+(rem*rem*rem)
    og=og//10
if sum==num:
    print("The entered number is armstrong")
else:
    print("Tne entered number is not armstrong")
