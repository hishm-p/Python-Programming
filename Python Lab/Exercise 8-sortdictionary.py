def new_dict():
        lim=int(input("Enter the no of entries:"))
        a={}
        for i in range(0,lim):
                key=input("Enter the key:")
                value=input("Enter the value:")
                a[key]=value
        return a
        
dict1=new_dict()

print (dict1)

print ("The Sorted dictionary  in ascending is:",sorted(dict1.items()))

print ("The Sorted dictionary  in descending is:",sorted(dict1.items(),reverse=True))
