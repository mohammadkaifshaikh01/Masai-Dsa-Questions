def sum_of_multiples(X, K, Y):
   add = 0
   mul = X*K
   i = 0
   while i <= mul:
      if i % X == 0 and  i % Y == 0:
         add+=i
      i+=1
   print(add)






X,K,Y = map(int,input("Enter : ").split())
sum_of_multiples(X, K, Y)