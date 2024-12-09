def sum_numbers_mod_k(num, K):


   while K < num:
      if K % 2 == 0:
         print(K)
      K+=1
   # print(add)7 27
    


num,K = map(int,input("Enter : ").split())
sum_numbers_mod_k(num,K)