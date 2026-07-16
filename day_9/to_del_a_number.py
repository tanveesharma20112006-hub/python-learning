numbers = [1, 2, 3, 2, 4, 2, 5]

num = int(input("Enter the number to delete: "))

new_list = []

for i in numbers:
    if i != num:
        new_list.append(i)

print("Updated list:", new_list)