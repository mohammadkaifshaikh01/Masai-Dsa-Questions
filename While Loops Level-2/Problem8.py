def sum_of_even_and_odd_numbers(N):
   even = 0
   i = 0
   odd = 0
   while i <= N:
      if i % 2 == 0:
         even+=i
      else:
         odd+=i
      i+=1
   if odd > even:
      print("odd")
   else:
      print("even")


    


N = int(input())
sum_of_even_and_odd_numbers(N)