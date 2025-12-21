from player import Player
from scores import save_player,view,TopScore,reset
from race import race_pick, show_race
from inventory import Inventory
from shop import shop_menu
'''
time developed: 44 hours + 179 hours from first prototype.
15 hours+ spent on learning classes,io, and __name__
--------------------------updates--------------------------
V1.0:creating main.py,scores.py,player.py
V1.1:creating inventory.py,enemy.py
V1.2:updating inventory.py,enemy.py and creatinf battle.py
v1.3:creating shop.py, race.py and creating ranks
----------------------UpcomingFeature----------------------
1.Skills
2.more enemy choices
3.crafting
4.better UI
5.converting to LUA
6.converting into pygame
7.converting into .exe
8.convertinf into .apk
9.using cv2
10.using socket
------------------------------------------------------------
'''
name=input("whats your name?")
show_race()
pick=int(input("what race you want to pick? "))-1
race,hp,strength,defense,level=race_pick(pick)

player=Player(name,race,hp,strength,defense,level)
print(player)
shop_menu(player)
