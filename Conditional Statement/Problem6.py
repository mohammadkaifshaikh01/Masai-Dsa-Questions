def compare_sums(a, b, c, d, e, f, g):
   sum1 = (a+b)*c
   sum2 = d+e+f+g

   if sum1 > sum2:
      print("true")
   else:
      print("false")



a, b, c, d, e, f, g = map(int,input("Enter Number : ").split())
compare_sums(a, b, c, d, e, f, g)