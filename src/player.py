from inventory import Inventory
LIGHT_GREEN = "\033[1;32m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
END = "\033[0m"
race_color={
    "Elf":LIGHT_GREEN,
    "Orc":GREEN,
    "Demon":RED,
    "Human":YELLOW
}
rank=[("F",20),("E-",10),("E",10),("E+",10),("D-",20),("D",20),("D+",20),("C-",30),("C",30),("C+",30),("B-",40),("B",40),("B+",40),("A-",50),("A",50),("A+",50),("S",70)]
class Player:
	def __init__(self, name,race="none", hp=0, strength=0, defense=0, level=1, weapon="Empty", health_potion=0, mana_potion=0,gold=200 ,armor="Empty"):
		self.name = name
		self.race = race
		self.hp = max(0,hp)
		self.strength = max(0,strength)
		self.defense = max(0,defense)
		self.level = max(1,level)
		self.weapon=weapon
		self.gold=gold
		self.health_potion=max(0,health_potion)
		self.mana_potion=max(0,mana_potion)
		self.armor=armor
		requirements=0
		for ranks,amount in rank:
			total = self.hp + self.strength + self.defense
			requirements+=amounta
			if total>=requirements:
				self.rank=ranks
        # If no inventory is given, start with an empty list
		self.inventory =Inventory(self.weapon,self.health_potion,self.mana_potion,self.gold,self.armor)
	def take_damage(self,enemy):
		dmg_taken=max(0,enemy.strength-self.defense)
		print(f"you've taken {dmg_taken} damage")
		return dmg_taken
	def attack(self,enemy):
		damage=max(0,self.strength-enemy.defense)
		enemy.hp=max(0,enemy.hp-damage)
		print(f"you've dealth {damage} damage")
		if enemy.hp==0:
			loot=enemy.drop_loot()
			if loot=="nothing":
				None
			else:
				for item,amount in loot:
					self.inventory.add_item(item,amount)
			return damage
	def add_hp(self,points):
		self.hp=max(0,self.hp+points)
	def add_str(self,points):
		self.strength=max(0,self.strength+points)
	def add_defs(self,points):
		self.defense=max(0,self.defense+points)
	def tuple(self):
		return(self.name,self.hp,self.strength,self.defense)
	@property
	def total(self):
		return self.hp+self.strength+self.defense
	@property
	def power(self):
		return self.total+self.level
	def show_inventory(self):
		return f"{'':-<40}Inventory:\n{self.inventory}\n{'':—<40}"
	def __str__(self):
		color=race_color.get(self.race,"")
		return f"{self.name:<10}{'level'}:{self.level}\n{'':—<20} \nRank:{self.rank}\nRace: {color}{self.race}{END}\nHP: {RED}{self.hp}{END}\nSTR: {YELLOW}{self.strength}{END}\nDEF: {BLUE}{self.defense}{END}\n{'':—<20}"
