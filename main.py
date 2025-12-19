from player import Player
from scores import save_player,view,TopScore,reset
from inventory import Inventory 
reset()
p1=Player("justin",level=10,hp=24, strength=45, defense=64,health_potion=5,mana_potion=3,weapon="sword",armor="iron armor")

print(p1)
save_player(p1)
p1.inventory.add_item("health potion")
p1.add_hp(21)
print(p1)
save_player(p1)
input("click enter to continue")

p2=Player("Cain", strength=21,hp=55,defense=21,weapon="dagger",health_potion=12,mana_potion=14,armor="steel armor")
print(p2)
p2.add_str(12)
p2.add_defs(42)
print(p2)
save_player(p2)
input("click enter to continue")
view()
TopScore()
input("click enter to continue")