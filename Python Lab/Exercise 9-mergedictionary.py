def new_dict():
        lim=int(input("Enter the no of entries:"))
        a={}
        for i in range(0,lim):
                key=input("Enter the key:")
                value=input("Enter the value:")
                a[key]=value
        return a

print("Enter the first dictionary \n")        
dict1=new_dict()
print("\nEnter the second dictionary \n")
dict2=new_dict()

def Merge(dict1, dict2):
	return(dict1.update(dict2))

Merge(dict1, dict2)

print("The dictionary after merging is:",dict1)
