def LargerNumberIdentifier(n1,n2):
   if n1 > n2:
      print(f"{n1} is larger than {n2}")
   elif n1 == n2:
      print("Both number is equal")
   else:
      print(f"{n1} is smaller than {n2}")




n1 = int(input("Enter Num1 : "))
n2 = int(input("Enter Num2 : "))
LargerNumberIdentifier(n1,n2)