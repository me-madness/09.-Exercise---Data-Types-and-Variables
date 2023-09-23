n = int(input())
count_of_litters = 0


for litter in range(1, n + 1):
    litters_income = int(input())
    count_of_litters += litters_income
    if count_of_litters >= 255:
        print("Insufficient capacity!")
        print(count_of_litters - litters_income)
        break

print(count_of_litters) 