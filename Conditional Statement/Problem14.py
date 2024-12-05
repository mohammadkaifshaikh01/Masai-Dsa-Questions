def check_fuel_distance(fuel, distance):
   required = fuel * distance
   if required > 50:
      print("Enough")
   else:
      print("Go On")
   


fuel = int(input("Fuel : "))
distance = int(input("distance : "))
check_fuel_distance(fuel,distance)