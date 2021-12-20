def pyramid(N):
    for i in range(1,N+1):
        print()
        for j in range(1,i+1):
            print("*",end=" ")
    for i in range(N-1,0,-1):
        print()
        for j in range(i+1,1,-1):
            print("*",end=" ")       

N=int(input("Enter the maximum no.of stars in a row for the pyramid:"))
pyramid(N)
