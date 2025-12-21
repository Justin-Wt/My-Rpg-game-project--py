from player import Player
from inventory import Inventory
YELLOW = "\033[1;33m"
END = "\033[0m"
shop_items=[
	("health potion",50),
	("mana potion",150),
	("sword", 1000),
	("iron armor",1500)]
def shop_menu(player):
	print(f"welcome to the shop {player.name}\nwhat would you like to do?\n{'':-<30}\n1. Buy\n2. Sell")
	choice=input(">")
	try:
		choice=int(choice)
	except ValueError:
		print("thats not a choice")
	else:
		if choice==1:
			buy()
		elif choice==2:
			sell()
		else:
			print("that not an option")
def item_shop():
	print(f"{'Buy':-^36}\n|No|{'Item':<20}|{YELLOW}{'Price':^10}{END}|\n{'':-<36}")
	for index,(item,price) in enumerate(shop_items,start=1):
		print(f"|{index:<2}|{item:<20}|{YELLOW}{price:<5} gold{END}|")
	print(f"{'':-<36}")
def buy(player):
	item_shop()
	print("what would you like to buy?")
	choice=input(">")
	try:
		choice=int(choice)-1
	except ValueError:
		print("thats not a choice")
	else:
		if 0<=choice<len(shop_items):
			item,price=shop_items[choice]
			if player.inventory.gold>=price:
				player.inventory.remove_item("gold",price)
				player.inventory.add_item(item)
				print(f"you bought {item} for {price} gold")
			else:
				print("not enough gold")
		else:
			print("thats not an option")
def sell(player):
	shop_price=dict(shop_items)
	print(f"{'sell':-^40}\n|No|{'Item':<15}|{'amount':^8}|{YELLOW}{'Price':^10}{END}|\n{'':-<40}")
	for index,(item,amount) in enumerate(player.inventory.items.items(),start=1):
		print(f"|{index:<2}|{item:<15}|{amount:<8}|{YELLOW}{int(0.5*shop_price.get(item)):<10}{END}|")
	print(f"{'':-<40}")
	print("which item do you want to sell?")
	choice=input(">")
	try:
		choice=int(choice)-1
	except ValueError:
		print("thats not a choice")
	else:
		your_item=list(player.inventory.items.keys())
		if 0<=choice<len(your_item):
			item=your_item[choice]
			
			sell_price=0.5*shop_price.get(item,10)
			player.inventory.remove_item(item)
			player.inventory.add_item("gold",sell_price)
			print(f"you have sold {item} for {int(sell_price)} gold")
		else:
			print("thats not an option")
if __name__=="__main__":
	player=Player("justin")
	player.inventory.add_item("gold",1000)
	print(player.inventory)
	shop_menu(player)
	print(player.inventory)
	input()
