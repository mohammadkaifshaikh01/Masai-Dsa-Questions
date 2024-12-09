def count_numbers_divisible_by_k(left, right, k):
   count = 0
   while left < right:
      if left % k == 0:
         count+=1
      left+=1
   print(count)
  

left = int(input("l : "))
right = int(input("R : "))
k = int(input("k : "))
count_numbers_divisible_by_k(left, right, k)