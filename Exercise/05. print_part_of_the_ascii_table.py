start_number = int(input())
stop_number = int(input())
output = ''
for i in range(start_number, stop_number + 1):
    output_letters = i
    output += str(chr(output_letters))  

print(output, end=" ")      