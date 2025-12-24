import json
from entity import Entity
from inventory import Inventory
from race import  race_pick
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
rank=[("F",40),("E-",10),("E",10),("E+",10),("D-",20),("D",20),("D+",20),("C-",30),("C",30),("C+",30),("B-",40),("B",40),("B+",40),("A-",50),("A",50),("A+",50),("S",70)]
class Player(Entity):
	def __init__(self, name,race="none", hp=0, strength=0, defense=0, weapon="Empty", health_potion=5, mana_potion=0,gold=200 ,armor="Empty", accessory1="Empty",accessory2="Empty"):
		super().__init__(name,hp,defense,strength)
		self._level=1
		self.xp=0
		self.race = race
		self.weapon=weapon
		self.gold=gold
		self.health_potion=max(0,health_potion)
		self.mana_potion=max(0,mana_potion)
		self.armor=armor
		self.accesory1=accessory1
		self.accesory2=accessory2
		accessories = []
		if accessory1 != "Empty":
		    accessories.append(accessory1)
		if accessory2 != "Empty":
		    accessories.append(accessory2)
		items = {
		    "health potion": health_potion,
		    "mana potion": mana_potion
		}
		self.inventory = Inventory(
            weapon=[weapon] if weapon != "Empty" else [],
            armor=[armor] if armor != "Empty" else [],
            gold=gold,
            items=items,
            accessories=accessories
        )
	def save(self,file):
	    data={
	        "name":self.name,
	        "race":self.race,
	        "level":self._level,
	    	"xp":self.xp,
	    	"hp":self.hp,
	    	"str":self.strength,
	    	"def":self.defense,
	    	"weapon":self.weapon,
    		"gold":self.gold,
	    	"hp potion":self.health_potion,
	    	"mana potion":self.mana_potion,
	    	"armor":self.armor,
	    	"accessory 1":self.accesory1,
	    	"accessory 2":self.accesory2,
	    	"inventory":{
	    	    "weapon":self.inventory.weapon,
	    	    "armor":self.inventory.armor,
	    	    "gold":self.inventory.gold,
	    	    "items":self.inventory.items,
	    	    "accessories":self.inventory.accessories
	    	}
	    }
	    with open(file,"w") as sv:
	        json.dump(data,sv,indent=4)
	
	@classmethod
	def load(cls,file):
	    with open(file,"r") as ld:
	        data=json.load(ld)
	    player=cls(
	        name=data["name"],
	        race=data.get("race","none"),
	        hp=data.get("hp",0),
	        strength=data.get("str",0),
	        defense=data.get("def",0),
	        weapon=data.get("weapon","Empty"),
	        health_potion=data.get("hp potion",0),
	        mana_potion=data.get("mana potion",0),
	        gold=data.get("gold",0),
	        armor=data.get("armor","Empty"),
	        accessory1=data.get("accessory 1","Empty"),
	        accessory2=data.get("accessory 2","Empty")
	    )
	    player._level=data.get("level", 1)
	    player.xp=data.get("xp",0)
	    inventory_data=data.get("inventory",{})
	    player.inventory=Inventory(
	        weapon=inventory_data.get("weapon",[]),
	        armor=inventory_data.get("armor",[]),
	        gold=inventory_data.get("gold",0),
	        items=inventory_data.get("items","Empty"),
	        accessories=inventory_data.get("accessories","Empty")
	    )
	    return player
	def add_hp(self,points):
		self.hp=max(0,self.hp+points)
	def add_str(self,points):
		self.strength=max(0,self.strength+points)
	def add_defs(self,points):
		self.defense=max(0,self.defense+points)
	def tuple(self):
		return(self.name,self.hp,self.strength,self.defense)
	def add_xp(self,xp):
	    self.xp+=xp
	@property
	def level(self): 
	    while self.xp>=5*self._level+6:
	        
	        self.xp-=5*self._level+6
	        self._level+=1
	    return self._level
	@property
	def ranks(self):
		requirements=0
		for ranks,amount in rank:
			total = self.hp + self.strength + self.defense
			requirements+=amount
			if total>=requirements:
				self.rank=ranks
			else:
				self.rank="F"
		return self.rank
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
		return f"{self.name:<10}{'level'}:{self.level}\n{'':—<20} \nRank:{self.ranks}\nRace: {color}{self.race}{END}\nXp: {self.xp}/{5*self._level+6}\nHP: {RED}{self.hp}{END}\nSTR: {YELLOW}{self.strength}{END}\nDEF: {BLUE}{self.defense}{END}\n{'':—<20}"
if __name__ == "__main__":
	race,hp,defense,strength=race_pick(2)
	player=Player("justin",race,hp,strength,defense)
	print (player)
	print("test")
	player.add_xp(27)
	print("run")
	player.save("save_slot1.json")
	print(player)
	print(player.inventory)
	
	input()
