def sum_of_digits(N):
   add = 0
   i = 0
   while i <= N:
      add+=i
      i+=1
   print(add)




N = int(input())
sum_of_digits(N)