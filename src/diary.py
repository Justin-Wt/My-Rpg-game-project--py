'''
progression≈17% done
Day passed:10 days
time developed: 67 hours + 179 hours from first prototype.
38 hours spent on develoment and handling errors
24 hours+ spent on learning
5 hours – problem solving & algorithm practice:
    -(HackerRank)
--------------------------updates--------------------------
V1.0:creating main.py,scores.py,player.py
V1.1:creating inventory.py,enemy.py
V1.2:updating inventory.py,enemy.py and creating battle.py
V1.3:creating shop.py,race.py and creating ranks
V1.4:updating race.py,enemy.py
V1.5:making diary.py
V1.6:making save and load system using json file
V1.7:making entity.py and status.py
----------------------UpcomingFeature----------------------
1.enemy special attack
2.duration for special attack
3.player special attack
4.ATB
5.making def equip armor,weapon,accessory
6.Skills
7.more enemy choices
8.crafting
9.better UI
10.converting to LUA
11.converting into pygame
12.converting into .exe
13.converting into .apk
14.using cv2
15.using socket
possible Remake:---------------Imaginations---------------
1.Town Npc
2.2D Open World
3.Companion
4.enemy spawn and AI movement in map
5.3D open world
6.Multiplayer mode
7.Seasonal Events
8.HDR visual
|------------------------RemakeSteps------------------------|--------------------------------------------|
|--------step-by-step-evolution-and-things-i-learned--------|-----------The-Function-I-Learned-----------|
|EnemySimulation.py----------------------------------7-Hours|--------------------------------------------|
|1.a code to print enemy name                               |-print()                                    |
|2.a code to input something                                |-input()                                    |
|3.a code to print a variables                              |-print(var) and print(f"{}")                |
|4.a code to decrease an integer                            |-var-=attack                                |
|6.a code to print my hp                                    |-print(f"{my_hp}")                          |
|7.a code to do a little battle                             |-while true: attack()                       |
|Rpg.py--------------------------------------------169-Hours|--------------------------------------------|
|1.a code to choose random enemy                            |-random.randrange(1,total)                  |
|2.a code to keep each enemy hp and attack                  |-if x==1: name="goblin"                     |
|3.a code to make battle loop                               |-While True:if my_hp<0:print(}              |
|4.a code to make def                                       |-def battle():                              |
|5.a code to make main menu                                 |-def main_menu():                           |
|6.a code to make main menu connected to the battle         |-if choice==1: battle()                     |
|7.a code to make intro                                     |-print("do you want to play?")              |
|8.a code to input my name                                  |-name=input("whats your name?")             |
|9.a code to make inventory                                 |-inventory=[]                               |
|10.a code to make status                                   |-print(f"name:{name}")                      |
|11.a code to make level                                    |-level=1                                    |
|12.a code to make xp                                       |-if xp>=req: level+=1                       |
|13.a code to randomize enemy level                         |-level=random.randrange(1,11)               |
|14.a code to count skill point                             |-sp=3*level                                 |
|15.a code to make stats                                    |-str=5,defs=7                               |
|16.a code to upgrade stats                                 |-if choice==str and amount==n str+=n        |
|17.a code to make colors                                   |-RED="\033[0;31m"                           |
|18.a code to make races                                    |-race=["Elf","Orc","Demon","Human"]         |
|19.a code to apply base stat per race                      |-if race=="Elf": Hp=n, str=a                |
|20.a code to make evolution for each race                  |-if race==''and level>=25:chose evo         |
|21.a code to use defense system                            |-enemy_attack=str*enemy_level-defs          |
|22.a code to randomize crit attack                         |-random.randrange(0,6) if 5: crit!          |
|23.a code to get gold                                      |-gold=random.randrange(0,1000)              |
|24.a code to randomize loot                                |-loot=[] if random=1: loot[1]               |
|25.a code to organize inventory                            |-def item() def equipment()                 |
|26.a code to make shop                                     |-for i,(itm,prc) in enumerate(shop.items()) |
|27.a code to auto delete                                   |-os.system('cls') and os.system('close')    |
|28.a code to make potion                                   |-if use_potion:hp+=20, potion-=1            |
|29.a code to make skill per race                           |-if race=="Elf":skill.append("doublearrow") |
|30.a code to use skill                                     |-if race==''andChoice==n:long attack format |
|project-rebuild-rpg--------------------------------56-hours|--------------------------------------------|
|1.class                                                    |class Player: def__init__(self,name)        |
|2.auto inputting                                           |def __init__(self,name):self.name=name      |
|3.returning player profile                                 |def__str__(self):return f"name:{self.name}" |
|4.importing class                                          |from player import Player                   |
|5.using imported class                                     |player=Player("justin")                     |
|6.saving game with txt                                     |with open("save.txt","w") as saving:        |
|7.one line sorting total tuples value                      |ranks.sort(key=lambda a:a[],reverse=true)   |
|8.printing item in tuples in one line                      |my_stat=", ".join(stats), print(my_stat)    |
|9.handling error for saving                                |except FileNotFoundError:pass               |
|10.one line print value for tuples                         |print(f"{dat}:{value}"for value,dat in lst) |
|11.counting total stat using property                      |@property def total(self):return self.hp+.. |
|12.picking enemy with classmethod                          |@classmethod def enemy():return cls(...)    |
|13.battling using staticmethod                             |@staticmethod def attack(atckr,dfndr):....  |
|14.using random with commas for drop chances               |amount=random.uniform(min,max)              |
|15.using only 1 variable to access tuples and dict         |tuples=["itm",5].for x in tuples:print(x[1])|
|16.using json to save file                                 |with open(save_slot.json) as save:          |
----------------------------------------------------------------------------------------------------------
Current focus: Game architecture, state management, and combat systems
Future College Major:Computer Science
----------------------------------------------------------------------------------------------------------
'''