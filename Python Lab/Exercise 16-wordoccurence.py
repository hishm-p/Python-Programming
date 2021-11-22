a=input("Enter the line of text").split(" ")
word={}
for i in range(0,len(a)):
    if a[i] not in word.keys():
        word[a[i]]=1
    else:
        n=word[a[i]]
        n=n+1
        word[a[i]]=n
for i in word:
    print(i,":",word[i])
    
   
        
