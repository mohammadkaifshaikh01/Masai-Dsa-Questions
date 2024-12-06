def SimpleInterestCalculator(p,r,t):
   Si = (p*r*t)/100
   print(f"The simple interest is: {Si}")


p = int(input("Enter Principle : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Time : "))
SimpleInterestCalculator(p,r,t)