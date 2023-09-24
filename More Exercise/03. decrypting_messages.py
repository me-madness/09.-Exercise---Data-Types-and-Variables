key = int(input())
n = int(input())
total_sum = 0
messages = 0
new_message = 0
for letter in range(1, n + 1):
    total_sum = 0
    messages = 0
    new_letter = input()
    total_sum += ord(new_letter)
    messages = total_sum + key
    print(chr(messages), end="")
