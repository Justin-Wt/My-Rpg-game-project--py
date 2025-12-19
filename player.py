from inventory import Inventory
class Player:
	def __init__(self, name, hp=0, strength=0, defense=0, level=1, weapon="Empty", health_potion=0, mana_potion=0, armor="Empty"):
		self.name = name
		self.hp = max(0,hp)
		self.strength = max(0,strength)
		self.defense = max(0,defense)
		self.level = max(1,level)
		self.weapon=weapon
		self.health_potion=max(0,health_potion)
		self.mana_potion=max(0,mana_potion)
		self.armor=armor
        # If no inventory is given, start with an empty list
		self.inventory =Inventory(self.weapon,self.health_potion,self.mana_potion,self.armor)
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
	
	def __str__(self):
		total = self.hp + self.strength + self.defense
		return f"{self.name:<12}{'level':>25}:{self.level}\n{'':—<40} \n HP: {self.hp}\n STR: {self.strength}\n DEF: {self.defense}\n Total: {total}\n{'':—<40}\nInventory:\n{self.inventory}\n{'':—<40}"
