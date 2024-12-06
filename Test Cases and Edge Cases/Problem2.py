def DiscountPriceCalculator(price):
   if price > 20:
      discount = float(price * 0.9)
      print(f"The final price of the item is : {discount} ")
   elif price == 20:
      print("No Discount Available" , price)
   elif price < 0:
      print("Invalid Price")




price = int(input("Enter Price : "))
DiscountPriceCalculator(price)