def check(arr):
   mini = float("inf")
   maxi = float("-inf")
   for i in range(len(arr)):
      if arr[i] > maxi:
         maxi = arr[i]
      if arr[i] < mini:
         mini = arr[i]
   print(maxi,mini)






arr = [3,5,8,9,10,11]
check(arr)