from player import Player
from inventory import Inventory
YELLOW = "\033[1;33m"
END = "\033[0m"
shop_items=[
	("health potion",50),
	("mana potion",150),
	("sword", 1000),
	("iron armor",1500)]
def buy_item(player, item, price,amount=1):
    if not player.inventory.gold >= price*amount:
        return False, "not enough gold"
    total_price=price*amount
    player.inventory.remove_item("gold", price*amount)
    player.inventory.add_item(item,amount)
    return True, f"you bought {amount} {item} for {total_price} gold"


def sell_item(player, item, price,amount):
    owned = player.inventory.items.get(item, 0)
    if amount>owned:
        return False, f"you dont have that many item in your inventory"
    total_price=int(price*0.5*amount)
    player.inventory.remove_item(item, amount)
    player.inventory.add_item("gold", total_price)
    return True, f"you sold {amount} {item} for {total_price}"
