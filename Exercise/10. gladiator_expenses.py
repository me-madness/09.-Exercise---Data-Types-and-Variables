lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
helmet_count = 0
sword_count = 0
shield_count = 0
armor_count = 0
helmet = 0
sword = 0
shield = 0
armor = 0
for fight in range(1, lost_fight_count + 1):
    if fight % 2 == 0:
        helmet = 0
        helmet_count += 1 
    if fight % 3 == 0:
        sword = 0
        sword_count += 1
        if fight % 2 == 0:
            sword = 0
            helmet_count += 1
    if helmet == 0 and sword == 0:
        shield = 0
        shield_count += 1
    if shield_count == 2:
        armor = 0
        armor_count += 1
        
expenses = int((helmet_count * helmet_price) + (sword_count * sword_price) + (shield_count * shield_price) + (armor_count * armor_price))            
print(f"Gladiator expenses: {expenses} aureus")