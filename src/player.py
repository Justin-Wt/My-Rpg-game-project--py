import json
import random
from entity import Entity
from status import StatusEffect,create_status
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

class Player(Entity):
	def __init__(self, name,race="none", hp=0, strength=0, defense=0, used_skill_point=0,weapon="Empty", health_potion=5, mana_potion=5,armor="Empty", accessory1="Empty",accessory2="Empty",speed=80,skill1=None,skill2=None):
		self.skills = {
            "Attack": self.basic_attack,
            "Double Arrow": self.double_arrow,
            "Sharp Arrow": self.sharp_arrow,
            "Throw": self.throw,
            "Heavy Attack": self.heavy_attack,
            "Life Steal": self.life_steal,
            "Rage": self.rage,
            "Triple Slash": self.triple_slash,
        }
		super().__init__(name,hp,defense,strength)
		self.atb=0
		self.speed=speed
		self.action_selected=None
		self.cast_time=0
		self._level=1
		self.xp=0
		self.race = race
		self.weapon=weapon
		self.used_skill_point=0
		self.health_potion=max(0,health_potion)
		self.mana_potion=max(0,mana_potion)
		self.armor=armor
		self.skill1=skill1
		self.skill2=skill2
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
            items=items,
            accessories=accessories)
    
	def save(self,file):
	    data={
	        "name":self.name,
	        "race":self.race,
	        "level":self._level,
	    	"xp":self.xp,
	    	"hp":self.hp,
	    	"str":self.strength,
	    	"def":self.defense,
	    	"used_skill_point": self.used_skill_point,
	    	"weapon":self.weapon,
	    	"hp potion":self.health_potion,
	    	"mana potion":self.mana_potion,
	    	"armor":self.armor,
	    	"accessory 1":self.accesory1,
	    	"accessory 2":self.accesory2,
	    	"skill1":self.skill1,
	    	"skill2":self.skill2,
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
	def unlock_skills(self):
	   if self.level >= 3 and "Double Arrow" not in self.skills:
            self.skills["Double Arrow"] = self.double_arrow
	def add_xp(self,amount):
	    self.xp+=amount
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
	        used_skill_point = data.get("used_skill_point", 0),
	        weapon=data.get("weapon","Empty"),
	        health_potion=data.get("hp potion",0),
	        mana_potion=data.get("mana potion",0),
	        armor=data.get("armor","Empty"),
	        accessory1=data.get("accessory 1","Empty"),
	        accessory2=data.get("accessory 2","Empty"),
	        skill1=data.get("skill1","Empty"),
	        skill2=data.get("skill2","Empty")
	    )
	    player._level=data.get("level", 1)
	    player.xp=data.get("xp",0)
	    inventory_data=data.get("inventory",{})
	    player.inventory=Inventory(
	        weapon=inventory_data.get("weapon",[]),
	        armor=inventory_data.get("armor",[]),
	        gold=inventory_data.get("gold",0),
	        items=inventory_data.get("items",{}),
	        accessories=inventory_data.get("accessories",[])
	    )
	    return player
	def add_hp(self,points):
		if points>=self.current_skill_point:
		    points=self.current_skill_point
		self.hp=max(0,self.hp+points)
		self.used_skill_point+=points
	def add_str(self,points):
		if points>=self.current_skill_point:
		    points=self.current_skill_point
		self.strength=max(0,self.strength+points)
		self.used_skill_point+=points
	def add_defs(self,points):
		if points>=self.current_skill_point:
		    points=self.current_skill_point
		self.defense=max(0,self.defense+points)
		self.used_skill_point+=points
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
	def rank(self):
	   req=0
	   rank=[("F",40),("E-",10),("E",10),("E+",10),("D-",20),("D",20),("D+",20),("C-",30),("C",30),("C+",30),("B-",40),("B",40),("B+",40),("A-",50),("A",50),("A+",50),("S",70)]
	   current_rank=rank[0][0]
	   total = self.hp + self.strength + self.defense  # default
	   for name, requirement in rank:
	           
	           if total >= req:
	               current_rank = name
	               req+=requirement
	               
	           else:
	               break
	   return current_rank
	@property
	def total_skill_point(self):
	    sp=self._level*3
	    return sp
	@property
	def current_skill_point(self):
		current_sp=self.total_skill_point-self.used_skill_point
		return current_sp
	@property
	def total(self):
		return self.hp+self.strength+self.defense
	@property
	def power(self):
		return self.total+self.level
	def show_inventory(self):
		return f"{'':-<40}Inventory:\n{self.inventory}\n{'':—<40}"
	def update_atb(self,dt):
	    if not self.can_act:
	        return
	    if self.action_selected is None and self.atb<100:
	        self.atb+=self.speed*dt
	        if self.atb>=100:
	            self.atb=100
	def update_action(self,dt,enemy):
	    enemy.update_statuses()
	    if self.atb<100:
	        self.atb+=dt*self.speed
	    if self.atb>=100:
	        skill=self.skills.get(self.action_selected)
	        if skill:
	            skill(enemy)
	def basic_attack(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(1,2))-enemy.defense)
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def double_arrow(self,enemy):
	    for _ in range(2):
	        damage=max(0,int(self.strength*random.uniform(1,2))-enemy.defense)
	        enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def sharp_arrow(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(2,4))-enemy.defense)
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def throw(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(1,2))-enemy.defense)
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	    enemy.apply_status(create_status("stun"))
	def heavy_attack(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(1,2)*2)-enemy.defense)
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def life_steal(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(1,2))-enemy.defense)
	    self.hp+=damage*0.2
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def rage(self,enemy):
	    damage=max(0,int(self.strength*random.uniform(1,2)*1.5)-enemy.defense)
	    enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def triple_slash(self,enemy):
	    for _ in range(3):
	        damage=max(0,int(self.strength*random.uniform(1,2))-enemy.defense)
	        enemy.hp=max(0,enemy.hp-damage)
	    self.atb=0
	    self.action_selected=None
	def is_ready(self):
	    return self.atb==100 and self.action_selected is None
	def __str__(self):
		color=race_color.get(self.race,"")
		return f"{self.name:<10}{'level'}:{self.level}\n{'':—<20} \nRank:{self.rank}\nRace: {color}{self.race}{END}\nXp: {self.xp}/{5*self._level+6}\nHP: {RED}{self.hp}{END}\nSTR: {YELLOW}{self.strength}{END}\nDEF: {BLUE}{self.defense}{END}\n{'':—<20}\ntotal:{self.total}"
if __name__ == "__main__":
	race,hp,defense,strength,skill1,skill2=race_pick(2)
	
	player=Player("justin",race,hp,strength,defense,skill1=skill1,skill2=skill2)
	print (player)
	print("test")
	player.add_str(200)
	player.add_hp(200)
	player.add_defs(200)
	player.add_xp(20)
	print("run")
	player.save("save_slot1.json")
	print(player)
	print(player)
	print(player.inventory)
	
	input()
