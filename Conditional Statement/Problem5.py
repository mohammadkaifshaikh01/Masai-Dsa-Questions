def compare_sum(one,two,three,four,five):
   sum1 = one + two + three
   sum2 = four + five

   if sum1 > sum2:
      print("true")
   else:
      print("false")



one,two,three,four,five = map(int,input("Enter Number : ").split())
compare_sum(one,two,three,four,five)