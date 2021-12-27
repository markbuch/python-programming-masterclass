available_exits = ["north", "south", "east", "west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("aren't you glad you got out of there ")

# for i in range(21):
#     if i == 0:
#         continue
#     if i % 3 == 0:
#         continue
#     if i % 5 == 0:
#         continue
#     print(i)
#
# print("-" * 30)
# for i in range(20):
#     if i != 0 and i % 3 != 0 and i % 5 != 0:
#         print(i)
#