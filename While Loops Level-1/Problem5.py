def print_odd_numbers_up_to(N):
   i = 0
   while i <= N:
      if i % 2 != 0:
         print(i, end=" ")
      i+=1
   


N = int(input("Enter : "))
print_odd_numbers_up_to(N)