def sum_of_odd_numbers(num):
   sumi = 0
   i = 0
   while i <= num:
      if i % 2 != 0:
         sumi+=i
      i+=1
   print(sumi)

   

num = int(input())
sum_of_odd_numbers(num)