def compare_rectangles(l1, b1, l2, b2):
   area = l1 * b1
   area2 = l2 * b2
   perameter1 = 2*(l1+b1)
   perameter2 = 2*(l2+b2)

   if area > area2:
      print("true")
   else:
      print("false")
   
   if perameter1 > perameter2:
      print("true")
   else:
      print("false")


 

l1, b1, l2, b2 = map(int,input("Enter Number : ").split())
compare_rectangles(l1, b1, l2, b2)