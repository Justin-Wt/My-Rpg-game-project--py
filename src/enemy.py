import random
class Enemy:
	def __init__(self,name,hp=10,strength=5,defense=3,level=1,loot=None):
		self.name=name
		self.hp=hp
		self.strength=strength
		self.defense=defense
		self.level=level
		self.loot=loot if loot is not None else []
	def drop_loot(self):
		dropped_item=[]
		for index,(item,chance,amount) in enumerate(self.loot):
			roll=random.randint(1,100)
			index+=1
			if roll<=chance:
				dropped_item.append((item,amount))
				print(item)
		if not dropped_item:
			dropped_item="nothing"
		if dropped_item=="nothing":
			print(f"the {self.name} dropped nothing")
		else:
			print(f"the {self.name} has dropped", end=' ')
			print(",".join(f"{amount} {item}" for item,amount in dropped_item))
		return dropped_item
	def take_damage(self,player):
		dmg_taken=max(0,player.strength-self.defense)
		print(f"the {self.name} taken {dmg_taken} damage")
		return dmg_taken
	def attack(self,player):
		damage=max(0,self.strength-player.defense)
		player.hp=max(0,player.hp-damage)
		print(f"the {self.name} dealth {damage} damage")
	def __str__(self):
		return f"{self.name:<10} level:{self.level}\n{'':-<20}\nhp:{self.hp}\nstrength:{self.strength}\ndefense:{self.defense}\n{'':-<20}"

