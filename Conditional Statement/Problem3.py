def compare_and_add(num1, num2, num3):
    num = num1 + num3
   
    if num1 > num2:
        print("true")
    else:
        print("false")
    
    if num > num2:
        print("true")
    else:
        print("false")
        
num1,num2,num3 = map(int,input("Enter Number 3 Times").split())
compare_and_add(num1, num2, num3)