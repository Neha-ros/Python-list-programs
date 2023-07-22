print("Python program to remove empty strings from a list")
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]
for i in list1:
    if i == "":
        list1.remove("")
print(list1)