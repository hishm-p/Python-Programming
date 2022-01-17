def wordlength(a):
    longest_word = len(a[0])
    temp = a[0]
 
    for i in a:
        if(len(i) > longest_word):
 
            longest_word = len(i)
            temp = i
 
    print("The word with the longest length is", temp,"and length is", longest_word)
 
a=input("Enter a list of words: ")
a=a.split(" ")
wordlength(a)