from inventory import Inventory
class Player:
	def __init__(self, name, hp=0, strength=0, defense=0, level=1, weapon="Empty", health_potion=0, mana_potion=0,gold=200 ,armor="Empty"):
		self.name = name
		self.hp = max(0,hp)
		self.strength = max(0,strength)
		self.defense = max(0,defense)
		self.level = max(1,level)
		self.weapon=weapon
		self.gold=gold
		self.health_potion=max(0,health_potion)
		self.mana_potion=max(0,mana_potion)
		self.armor=armor
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
		total = self.hp + self.strength + self.defense
		return f"{self.name:<10}{'level'}:{self.level}\n{'':—<20} \n HP: {self.hp}\n STR: {self.strength}\n DEF: {self.defense}\n{'':—<20}"
