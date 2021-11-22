a=input("Enter the first list:- \n")
b=input("Enter the second list:- \n")
list1=list(map(int,a.split(" ")))
list2=list(map(int,b.split(" ")))
if len(list1)==len(list2):
    print("\nThe Lists are of same length ",len(list1))
else:
    print("\nThe Lists are not of same length\n")
sum1=sum(list1)
sum2=sum(list2)
if sum1==sum2:
    print("\nThe Lists sum to the same value ",sum1)
else:
    print("\nThe Lists do not sum to the same value\n")
commonvalue=[]
for i in list1:
    if i in list2:
          commonvalue.append(i)
print("\nThe common terms in both list are: ",commonvalue)          
          
    
