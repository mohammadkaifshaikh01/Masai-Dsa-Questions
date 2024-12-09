def sum_numbers_mod_k(num, K):
   add = 0

   while K < num:
      if K % 2 == 0:
         add+=K
      K+=1
   print(add)
    


num,K = map(int,input("Enter : ").split())
sum_numbers_mod_k(num,K)