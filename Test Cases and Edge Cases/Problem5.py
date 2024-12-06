def BMICalculator(weight,height):
   
   if height > 0 and weight > 0:
      BMI = round(weight/(height*height),2)
      print(f"Your BMI is : {BMI}")
   elif height <= 0 and weight <= 0:
      print("Please enter valid positive  values")
   elif height <= 0:
      print("Please enter valid value for height ")
   elif weight <= 0:
      print("Please enter valid value for weight ")
  




weight = int(input("Enter Your Weight : "))
height = float(input("Enter Your height : "))
BMICalculator(weight,height)