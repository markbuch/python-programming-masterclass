shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#  initial example
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

#  continue example
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)
#

# break example
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

