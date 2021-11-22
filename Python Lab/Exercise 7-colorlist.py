color_list1=input("Enter first list of colors:- ")
color_list1=set(color_list1.split(" "))
print(color_list1)
color_list2=input("Enter second list of colors:- ")
color_list2=set(color_list2.split(" "))
print(color_list2)
color_list3=color_list1.difference(color_list2)
print("The colors in List 1 which are not present in List 2 are:-",color_list3)
 
