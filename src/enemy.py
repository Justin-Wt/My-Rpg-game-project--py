import random
from entity import  Entity
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"
class Enemy(Entity):
    def __init__(self,name="None",level=1,base_hp=10,base_strength=3,base_defense=2,loot=None,drop_multi=1,special_attack=None):
       self.level=level
       hp=base_hp+3*level
       strength=base_strength+level
       defense=base_defense+level
       self.special_attack=special_attack if special_attack is not None else []
       super().__init__(name,hp,defense,strength)
       self.drop_multi=drop_multi
       self.loot=loot if loot is not None else []
       
    def attack(self,player):
        if self.special_attack is not None:
            for item in self.special_attack:
                special_attack_name,special_attack_chance,special_attack_damage= item
                chance=random.randint(1,100)
                if chance<=special_attack_chance:
                    damage=special_attack_damage if special_attack_damage is not None else 0
                    player.apply_status(special_attack_name)
                    player.hp=max(0,player.hp-damage)
                    print(f"the {self.name} use {special_attack_name} and dealt {damage}")
                    return damage
        else:
            damage=max(0,self.strength-player.defense)
            player.hp=max(0,player.hp-damage)
            print(f"the {self.name} dealt {damage} damage")
        return damage
        
    def drop_loot(self):
        dropped_item=[]
        for item,minimum,maximum in self.loot:
            amount=random.uniform(minimum,maximum)
            amount=int(amount*self.drop_multi)
            if amount>0:
                dropped_item.append((item,amount))
        return dropped_item
        
    @classmethod
    def from_area(cls, area, tier):
        ranks = {
            "normal": (1, 1, 1),
            "elite": (1.5, 1.3, 2),
            "boss": (3, 2, 5)
        }
        if tier not in ranks:
            return None
        hp_multi,strength_multi,drop_multi=ranks.get(tier)
        level=random.randint(1,20)
        areas={
            "forest": [
                ("Goblin",level, 10, 2, 1, [("gold", 75, 150),("goblin necklace",0,1)],[]),
		 	   ("Wolf",level, 12, 3, 4, [("gold", 80, 180),("fang",0,3)],[("double strike",30),("bleed",20)])
                ],
            "cave": [
                ("Slime",level, 8, 1, 0, [("gold", 5, 20),("slime gel", 1, 4),("health potion", 0, 1),("sticky core", 0, 0.1)],[("toxic spit",50)]),
                ("Bat", level, 9, 2, 1, [("gold",5,10),("bat wing", 0, 1),("echo dust", 0, 1),("blood vial", 0, 0.5),("bat fang", 0, 0.1)],["scream",30])
                ]
            }
        test_area = areas.get(area)
        if test_area is None:
            print("that's not a valid zone")
            return None
        name, lvl, hp, strength, defense, loot, special_attack= random.choice(test_area)

        return cls(
            name,
            lvl,
            int(hp * hp_multi),
            int(strength* strength_multi),
            defense,
            loot,
            drop_multi,
            special_attack
        )
    def __str__(self):
        return f"{self.name:<10} level:{self.level}\n{'':-<20}\n{RED}hp:{self.hp}{END}\n{YELLOW}strength:{self.strength}{END}\n{BLUE}defense:{self.defense}{END}\n{'':-<20}"
if __name__=="__main__":
    enemy=Enemy.from_area("cave","boss")
    print(enemy)
    enemy.drop_loot()
    input()
