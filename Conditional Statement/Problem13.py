def check_speed(distance, time):
   speed = distance / time

   if speed > 40:
      print("Apply Brake")
   else:
      print("Keep Moving")
    


distance = int(input("Distance : "))
time = int(input("time : "))
check_speed(distance, time)