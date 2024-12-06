def areaOfTriangle(base,height):
   area = (base*height)/2
   if area < 0:
      print("Invalid Number base amd height must be positive")
   else:
      print("The area of triangle is: ",area)






base = int(input("Enter Base : "))
height = float(input("Enter Height :"))
areaOfTriangle(base,height)