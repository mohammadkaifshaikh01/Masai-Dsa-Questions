# Square and Sum
def calculate_sum_of_squares(one, two, three):
   return (one*one) + (two*two) + (three*three)
    

one,two,three = map(int,input("Enter : ").split())
print(calculate_sum_of_squares(one, two, three))