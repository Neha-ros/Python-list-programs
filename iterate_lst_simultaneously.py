print("Python program to iterate lists simultaneously")
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100
list3 = list2[::-1]
for i in range(len(list1)):
    print(list1[i],list3[i])