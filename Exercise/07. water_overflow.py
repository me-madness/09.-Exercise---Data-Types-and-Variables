n = int(input())
count_of_litters = 0
capacity = 255
for litter in range(n):
    litters_income = int(input())
    if capacity - litters_income < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litters_income
    count_of_litters += litters_income
print(count_of_litters)


# for litter in range(n):
#     litters_income = int(input())
#     if capacity - litters_income > 0:
#         count_of_litters += litters_income
#         if count_of_litters > capacity:
#             print("Insufficient capacity!")
#             count_of_litters -= litters_income
#             continue
#     print(count_of_litters) 

# number_of_lines = int(input())
# water_counter = 0
# tank_capacity = 255
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:  # no enough capacity
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
#     water_counter += liters_of_water
# print(water_counter)

