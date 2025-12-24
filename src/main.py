from player import Player
from scores import view,TopScore,reset
from race import race_pick, show_race
from inventory import Inventory
from shop import shop_menu

name=input("whats your name?")
show_race()
pick=int(input("what race you want to pick? "))-1
race,hp,strength,defense,=race_pick(pick)

player=Player(name,race,hp,strength,defense)
print(player)
player.save("save_slot1.json")
shop_menu(player)
