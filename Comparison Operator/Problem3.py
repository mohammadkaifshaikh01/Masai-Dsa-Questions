# Product Of Six
def calculate_product(one, two, three, four, five, six):
   return one * two * three * four * five * six
   
one,two,three,four,five,six = map(int,input("Please Enter Your Six Number : ").split())
print(calculate_product(one, two, three, four, five, six))