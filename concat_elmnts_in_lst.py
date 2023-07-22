print("Python program to concatenate elements in a list")
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3 = []
for i in list1:
    for a in list2:
        y = i+a
        list3.append(y)
print(list3)