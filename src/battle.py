from player import Player
from enemy import Enemy
from inventory import Inventory
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"
def status(player,enemy):
	print(f"{'':-<55}\n|lv.{enemy.level:<2} {enemy.name:<20}|lv.{player.level:<2} {player.name:<20}|\n{'':-<55}\n|{RED}Hp:{enemy.hp:<23}{END}|{RED}Hp:{player.hp:<23}{END}|\n|{YELLOW}strength:{enemy.strength:<17}{END}|{YELLOW}strength:{player.strength:<17}{END}|\n|{BLUE}defense:{enemy.defense:<18}{END}|{BLUE}defense:{player.defense:<18}{END}|\n{'':-<55}")
player=Player("justin",hp=10,strength=12,defense=4,level=3,weapon="sword",armor="iron armor")
goblin=Enemy("goblin",hp=10,strength=7,defense=2,level=3,loot=[("gold",50,100),("health potion",40,5),("goblin scarf",10,1)])
status(player,goblin)
Enemy.attack(goblin,player)
Player.take_damage(player,goblin)
status(player,goblin)
Player.attack(player,goblin)
print(player.inventory)
input()