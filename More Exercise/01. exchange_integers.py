first_number = int(input())
second_number = int(input())

a = first_number
b = second_number
print(f"Before: \n a = {a}\n b = {b}")

temp = a
a = b
b = temp
print(f"After: \n a = {a}\n b = {b}")



