lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_count = lost_fight_count // 2
sword_count = lost_fight_count // 3
shield_count = lost_fight_count // (2 * 3)
armor_count = shield_count // 2
        
expenses = helmet_count * helmet_price \
            + sword_count * sword_price \
            + shield_count * shield_price \
            + armor_count * armor_price            
print(f"Gladiator expenses: {expenses:.2f} aureus")