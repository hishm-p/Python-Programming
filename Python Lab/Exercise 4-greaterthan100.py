a=input("Enter a sequence of strings:- \n")
a=list(map(int,a.split(" ")))
for i in range(0,len(a)):
    if a[i]>100 :
        a[i]="over"    
print(a)
