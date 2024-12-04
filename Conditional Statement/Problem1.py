user = int(input("Please Enter Your Number : "))

if user > 0:
   print("Your number is positive : " ,user)
elif user < 0:
    print("Your number is Negative : " ,user)
elif user == 0:
   print("Number is 0")
if user % 2 == 0:
   print("Even")
else:
   print("Odd")
