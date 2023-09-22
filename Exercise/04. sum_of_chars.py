n = int(input())
total_sum = 0

for letter in range(1, n + 1):
    new_letter = input()
    total_sum += ord(new_letter)

print(f"The sum equals: {total_sum}")