import random
import os
def delete():
	os.system('cls')
GRAY = "\033[1;30m"
END = "\033[0m"
class enemy:
	def __init__(self, name, level, base_hp,defense,scale):
		self.name=name
		self.level=level
		self.max_hp=base_hp+level*scale
		self.hp=self.max_hp
		self.defense=defense
	def __str__(self):
		return f"""
		you have encountere a level {level} {name}
		hp={self.max_hp}/{self.hp}
		defense={self.defense}
		""".strip()
class Item():
    def __init__ (self, name, effect='none'):
       self.name=name
       self.effect=effect
       self.quantity =1
    def __str__(self):
    	return f"{self.name} (x{self.quantity})"
class Equipment(Item):
	def __init__ (self,name,effect=None,equip_type=None):
		super().__init__(name,effect)
		self.equip_type=equip_type
class Inventory():
	def __init__(self):
		self.items={}
		self.equipped_weapon=None
		self.equipped_armor=None
	def show_equipment(self):
		print(f"sword={self.equipped_weapon}")
		print(f"armor={self.equipped_armor}")
		input(f"{GRAY}click enter to continue{END}")
		delete()
	def add_item(self, item):
		if item.name in self.items:
			self.items[item.name].quantity+=1
		else:
			self.items[item.name]=item
	def use_item(self,name):
		if name in self.items and self.items[name].quantity>0:
			self.items[name].quantity-=1
			print(f"you have used your {name}")
		elif self.items[name].quantity==0:
			print(f"you have ran out of {name}")
		else:
			print(f"you dont have any {name}")
		input(f"{GRAY}click enter to continue{END}")
		delete()
	def show_inventory(self):
		if not self.items:
			print("you dont have any items")
		else:
			print("-"*10+"Inventory"+"-"*10)
			for item in self.items.values():
				if isinstance(item, Equipment):
					print(f"{item.name}")
				else:
					print(item)
			print("-"*29)
		input(f"{GRAY}click enter to continue{END}")
		delete()
	def equip_item(self,name):
		if name in self.items:
			item=self.items[name]
			if not isinstance(item,Equipment):
				print(f"{item.name} is not equipable")
			elif item.equip_type=="armor":
				self.equipped_armor= item.name
				print(f"you have equipped {item.name} as your {item.equip_type}")
			elif item.equip_type=="sword":
				self.equipped_weapon=item.name
				print(f"you have equipped {item.name} as your {item.equip_type}")
		else:
			print(f"{GRAY}you dont have {name} in your inventory{END}")
		input(f"{GRAY}click enter to continue{END}")
		delete()
		
def enemy_loot(inventory):
	lootable=[
	{"item": Item("potion",effect="heal 20 hp"), "chance":50},
	{"item":Equipment("Iron Sword",effect="increases attack by 5",equip_type="sword"), "chance":30},
	{"item": Equipment("Iron Armor",effect="increases defense by 10", equip_type="armor"),"chance":20}]
	roll=random.randint(1,100)
	total_chance=0
	for loots in lootable:
		total_chance+=loots["chance"]
		if roll<=total_chance:
			loot=loots["item"]
			inventory.add_item(loot	)
			if isinstance(loot,Equipment):
				print(f"the monster dropped an equipment {loot.name}:{loot.equip_type}")
			else:
				print(f"the monster dropped {loot}")
			break
		else:
			print("the monster didnt drop anything")
			input(f"{GRAY}click enter to continue {END}")
			delete()
potion=Item("potion",effect="heal 20 hp")
iron_sword=Equipment("Iron Sword",effect="increases attack by 5",equip_type="sword")
iron_armor=Equipment("Iron Armor", effect= "increases defense by 10", equip_type="armor")

print(potion)
print(iron_sword)
print(iron_armor)
input("for items classis")

inv=Inventory()
inv.add_item(potion)
inv.add_item(potion)
inv.show_inventory()
inv.use_item('potion')
inv.show_inventory()
inv.add_item(iron_sword)
inv.add_item(iron_armor)
inv.show_inventory()
inv.equip_item("potion")
inv.equip_item("Iron Sword")
inv.equip_item("Iron Armor")
inv.show_inventory()
inv.show_equipment()
input("for Inventory classis")

enemy_loot(inv)
inv.show_inventory()
input("for looting class")
