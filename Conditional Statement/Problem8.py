def check_cube_vs_square(n, m):
   cube = n*n*n
   square = m*m
   if cube > square:
      print("true")
   else:
      print("false")
   
n,m =  map(int,input("Enter Number : ").split())
check_cube_vs_square(n,m)