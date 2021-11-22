list1=input("Enter a sequence of integers:- \n")
list1=list(map(int,list1.split(" ")))
odd_list=[i for i in list1 if i%2!=0]
print("The list after removing even numbers is:",odd_list)
