num=int(input("Enter a number to check whether it's armstrong or not: "))
l=len(str(num))
og=num
sum=0
while num!=0:
    rem=num%10
    sum += rem**l
    num=num//10

if sum==og:
    print(og,"is an armstrong number")
else:
    print(og,"is not an armstrong number")
