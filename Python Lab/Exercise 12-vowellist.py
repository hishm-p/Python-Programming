a=input("Enter the word to select the vowels from it: ")
a=list(a.strip())
print(a)
b=[i for i in a if i in 'AEIOUaeiou']
print("The list of vowels from the entered word is:",b)
