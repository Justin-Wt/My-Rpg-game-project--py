from player import Player
from enemy import Enemy
from inventory import Inventory
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"
def attack(attacker,enemy):
		damage=max(0,attacker.strength-enemy.defense)
		enemy.hp=max(0,enemy.hp-damage)
		print(f"you've dealth {damage} damage")
		enemy_damage=max(0,enemy.strength-attacker.defense)
		attacker.hp=max(0,attacker.hp-enemy_damage)
		print(f"The enemy has counter with {enemy_damage} damage!")
		if attacker.hp==0:
		    print("you've lost")
		elif enemy.hp==0:
			loot=enemy.drop_loot()
			if not loot:
				print(f"The {self.name} dropped nothing")
			else:
				print(f"the {self.name} has dropped:\n-",end='')
				for item,amount in loot:
					print(f"- {amount} {item}")
					attacker.inventory.add_item(item,amount)
			return damage
	
def status(attacker,enemy):
	print(f"{'':-<55}\n|lv.{enemy.level:<2} {enemy.name:<20}|lv.{attacker.level:<2} {attacker.name:<20}|\n{'':-<55}\n|{RED}Hp:{enemy.hp:<23}{END}|{RED}Hp:{attacker.hp:<23}{END}|\n|{YELLOW}strength:{enemy.strength:<17}{END}|{YELLOW}strength:{attacker.strength:<17}{END}|\n|{BLUE}defense:{enemy.defense:<18}{END}|{BLUE}defense:{attacker.defense:<18}{END}|\n{'':-<55}")

#battle test
if __name__=="__main__":
	player=Player("justin","Elf",hp=10,strength=2222222,defense=4,weapon="sword",armor="iron armor")
	enemy1=Enemy.from_area("forest","normal")
	status(player,enemy1)
	attack(player,enemy1)
	status(player,enemy1)
	attack(player,enemy1)
	status(player,enemy1)
	print(player.inventory)
	input()
