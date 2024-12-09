def is_prime(num):

   i = 2
   while i < num:
      if num % i == 0:
         print("No")
         break
      i+=1
   else:
      print("Yes")
      
    


num = int(input("Enter : "))
is_prime(num)