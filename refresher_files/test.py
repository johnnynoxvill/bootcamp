# # test.py: to try out other formulae

# # def give():
# #     return 5

# # def show():
# #     print(5)

# # def double(x):
# #     print(x * 2)
# def double(x):
#     return x * 2

# def add_one(x):
#     return x + 1

# def triple(x):
#     return x * 3

# a = double(3)
# b = add_one(a)
# c = double(b)


# result = double(4)
# print(result)

# # a = give()
# # b = show()
# # print(a + 1)
# # print(b)

temps = [50, 53, 49, 55]

previous = None
for current in temps:
    if previous is not None:
        print(f"changed by {current - previous}")
    previous = current