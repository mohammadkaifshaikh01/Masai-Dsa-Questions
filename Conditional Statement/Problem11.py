def compare_countries(Australia, England):
   if Australia > England:
      print("Australia")
   elif Australia < England:
      print("England")
   elif Australia == England:
      print("Tie")
   


Australia = int(input("Enter Australia : "))
England = int(input("Enter England : "))
compare_countries(Australia, England)