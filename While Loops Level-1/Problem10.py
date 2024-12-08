def count_even_numbers(N):
   i = 1
   count = 0
   while i <= N:
      if i % 2 == 0:
         count += 1
      i+=1
   print(count)

    


N = int(input())
count_even_numbers(N)