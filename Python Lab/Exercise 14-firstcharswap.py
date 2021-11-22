s1=input("Input first string: ")
s2=input("Input second String: ")
new_s1=s2[0]+s1[1:]
new_s2=s1[0]+s2[1:]
s3=new_s1+" "+new_s2
print("The Combined string with first characters swapped is:",s3)
