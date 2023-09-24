group_size = int(input())
days = int(input())
income_day_coins = 0

for day_count in range(1, days + 1):
    if day_count % 10 == 0:        
        group_size -= 2
    if day_count % 15 == 0:
        group_size += 5
    if day_count % 3 == 0:
        income_day_coins -= group_size * 3
    if day_count % 5 == 0:
        income_day_coins += group_size * 20
        if day_count % 3 == 0:
            income_day_coins -= group_size * 2
    income_day_coins += 50
    income_day_coins -= group_size * 2  
coins = int(income_day_coins / group_size)      
print(f"{group_size} companions received {coins} coins each.")