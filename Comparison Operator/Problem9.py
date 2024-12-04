def calculate_product(a, b, c, d, e, f, g):
   
   return (a+b+c) * (d+e+f+g)

a, b, c, d, e, f, g = map(int,input("Enter : ").split())
print(calculate_product(a, b, c, d, e, f, g))