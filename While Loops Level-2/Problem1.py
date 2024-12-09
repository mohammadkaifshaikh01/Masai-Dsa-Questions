def print_numbers_in_range(max_val, min_val):

   while min_val < max_val:
      print(min_val)
      min_val+=1
  

max_val = int(input("Enter Max : "))
min_val = int(input("Enter Min : "))
print_numbers_in_range(max_val, min_val)