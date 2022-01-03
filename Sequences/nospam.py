menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# my solution to the challenge
# for meal in menu:
#     if "spam" in meal:
#         for index in range(len(meal) - 1, -1, -1):
#             if meal[index] == "spam":
#                 del meal[index]
#         print(meal)
#     else:
#         print(meal)
# Paul's solution
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", " .join(meal))
    

