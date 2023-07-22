print("Python program to concatenate lists index wise")
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# ['My', 'name', 'is', 'Kelly']
list3 = []
for i in range(len(list1)):
    y= list1[i] + list2[i]
    list3.append(y)
print(list3)
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)