from player import Player
from enemy import Enemy,enemy_picker
from inventory import Inventory
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"
def status(player,enemy):
	print(f"{'':-<55}\n|lv.{enemy.level:<2} {enemy.name:<20}|lv.{player.level:<2} {player.name:<20}|\n{'':-<55}\n|{RED}Hp:{enemy.hp:<23}{END}|{RED}Hp:{player.hp:<23}{END}|\n|{YELLOW}strength:{enemy.strength:<17}{END}|{YELLOW}strength:{player.strength:<17}{END}|\n|{BLUE}defense:{enemy.defense:<18}{END}|{BLUE}defense:{player.defense:<18}{END}|\n{'':-<55}")

#battle test
if __name__=="__main__":
	player=Player("justin",hp=10,strength=2222222,defense=4,level=3,weapon="sword",armor="iron armor")
	enemy=enemy_picker(1)
	status(player,enemy)
	enemy.attack(player)
	player.take_damage(enemy)
	status(player,enemy)
	player.attack(enemy)
	status(player,enemy)
	print(player.inventory)
	input()
