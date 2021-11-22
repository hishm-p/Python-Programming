a=input("Enter a string to check it's reverse: ")
rev=a [::-1]
print("The Reverse of the entered string is: ",rev)
if a==rev:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
