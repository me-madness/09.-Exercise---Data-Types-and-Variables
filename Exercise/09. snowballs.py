snowballs = int(input())
new_value = 0
new_quality = 0
new_time = 0
new_weight = 0
for ball in range(1, snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if new_value < snowball_value:
        new_value = snowball_value
    if new_quality < snowball_quality:
        new_quality = snowball_quality       
    if new_time < snowball_time:
        new_time = snowball_time 
new_weight = int((new_value // new_quality) * new_time)             
print(f"{new_weight} : {new_time} = {new_value} ({new_quality})")