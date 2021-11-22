a=int(input("Enter a year to check whether it's leap year or not: "))
if(a%100==0):
   if(a%400==0):
      print(a,"is a leap year")
   else:
      print(a,"is not a leap year")
elif(a%4==0):
   print(a,"is a leap year")
else:
   print(a,"is not a leap year")
