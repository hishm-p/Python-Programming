num= int(input("Enter a number to check whether it's prime or not: "))
flag = 0
for i in range(2,num):
	if num % i == 0:
		flag = 1
if flag == 0:
    print(num,"is a Prime Number")
else: 
    print(num,"is a not Prime Number")