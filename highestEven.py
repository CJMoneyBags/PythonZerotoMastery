def highest_even(li):
#    maxNum = 0
#    for item in li:
#       if item % 2 == 0:
#          if maxNum > item:
#             return maxNum
#          else:
#             maxNum = item
#             return maxNum
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    if evens == []:
        return "No evens in list"
    else:
        return max(evens)

        

print(highest_even([1,2322,33,43,81,11]))