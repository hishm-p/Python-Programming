def pyramid(N):
    for i in range(1,N+1):
        print()
        for j in range(1,i+1):
            print(i*j,end=" ")

N=int(input("Enter the number of steps for the pyramid:"))
pyramid(N)


