print("Python program to add an item to a list")
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)