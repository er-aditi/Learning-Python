num_list = [10, 5, 70, 40, 80, 88, 4, 73, 7, 3]
# var = 0
# num = 0
# x = 1
# while num < len(num_list):
#     if num != len(num_list) - 1:
#         if num_list[num + 1] > num_list[num]:
#             var = num_list[num + 1]
#
#     num += 1
#
# print(var)

largest = num_list[0]
index = 1

while index < len(num_list):
    if num_list[index] > largest:
        largest = num_list[index]
    index += 1

print("Largest:", largest)

