def compare_operations(num1, num2):
   if num1 > num2:
      print("true")
   else:
      print("false")
   if num1 < num2:
      print("true")
   else:
      print("false")
   if num1 == num2:
      print("true")
   else:
      print("false")



    
num1,num2 = map(int,input("Enter Number : ").split())
compare_operations(num1, num2)