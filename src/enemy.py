import random
class Enemy:
	def __init__(self,name,level=1,base_hp=10, base_strength=5,base_defense=3,loot=None):
		self.name=name
		self.level=level
		self.hp=base_hp+3*level
		self.strength=base_strength+level
		self.defense=base_defense+level
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

def enemy_picker(choice=1):
		 if choice==1:
		 	level=random.randint(1,10)
		 	ENEMIES = [
		 	("Goblin",level, 10, 2, 1, [("gold", 100, 100),("goblin necklace",25,1)]),
		 	("Wolf",level, 12, 3, 4, [("fang", 30, 1)]),
		 	("Slime",level, 8, 1, 0, [("gold", 100, 5),("slime gel", 60, 1),("health potion", 25, 1),("sticky core", 5, 1)])
		 	]
		 	return Enemy(*random.choice(ENEMIES))

#enemy test
if __name__=="__main__":
	enemy1=enemy_picker(1)
	print(enemy1)
	drop_loot()
