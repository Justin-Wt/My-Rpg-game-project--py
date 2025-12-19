import random
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
YELLOW = "\033[1;33m"
END = "\033[0m"
GRAY = "\033[1;30m"
Rarity=[f"{YELLOW}Legendary{END}",f"{PURPLE}Epic{END}",f"{BLUE}Rare{END}",f"{GRAY}Common{END}"]
loot = [(f"Gold 💰 -{Rarity[3]}",50), (f"Armor 🦺 -{Rarity[2]}",25), (f"Shield 🛡️ -{Rarity[1]}",10), (f"Potion 🧪 -{Rarity[1]}",10), (f"Sword 🗡️ -{Rarity[0]}",5)]

print("🎉 You defeated the enemy! Let's see what you got:")
for i in range(3):
    total_chance=sum(chance for _,chance in loot)
    roll=random.randint(1,total_chance)
    current=0
    for index,(item,chance) in enumerate(loot):
        current+=chance
        if roll<=current:
            drop = item
            loot.remove((drop,chance))
            break
    
    print(f"  - {drop}")

input()