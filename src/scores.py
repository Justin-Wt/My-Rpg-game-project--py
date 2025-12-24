from player import Player
from inventory import Inventory
File="save_slot1.json"
def load_player():
	players=[]

	try:
		with open(File,"r") as stats:
			for indexs, rows in enumerate(stats,start=1):
				parts=rows.strip().split(":")
				if len(parts)!=12:
					print(f"skipping corrupted line: {rows}")
					print("error caused because its missing a stats")
					continue
				name,rank,race,hp,strength,defense,level,weapon,health_potion,mana_potion,gold,armor=parts
				try:
					players.append(Player(name, rank,race, int(hp), int(strength), int(defense),int(level),weapon,int(health_potion),int(mana_potion),int(gold),armor))
				except ValueError:
					print(f"[line{indexs}] is skipped because its corrupted line: {rows}")
					print("error caused because one of the variable has a false value")
					continue
	except FileNotFoundError:
		print("no file") 
	return players
def TopScore(lim=5):
		stats=load_player()
		stats.sort(key=lambda a:a.hp+a.strength+a.defense+a.level,reverse=True)
		print(f"{'here is the top 5 scores':-^67}")
		print("| No | Name                      | Total | Hp | STR | DEF | Level |")
		print("-------------------------------------------------------------------")
		for idx, a  in enumerate(stats[:lim], start=1):
			total=a.power
			print(f"| {idx:<3}| {a.name:<26}|{total:^7}| {a.hp:<3}| {a.strength:<4}| {a.defense:<4}| {a.level:^5} |" )
		print("-------------------------------------------------------------------")
def view():
		stats=load_player()
		print(f"{'your current scores':-^67}")
		print("| No | Name                      | Total | Hp | STR | DEF | Level |")
		print("-------------------------------------------------------------------")
		for idx, a in enumerate(stats, start=1):
			total=a.power
			print(f"| {idx:<3}| {a.name:<26}|{total:^7}| {a.hp:<3}| {a.strength:<4}| {a.defense:<4}| {a.level:^5} |")
		print("-------------------------------------------------------------------")
def reset():
		with open(File, "w") as scor:
			pass
		print("your save is deleted")
if __name__ == "__main__":
	player=Player("justin","F","Elf",21,23,21,100,"sword",12,11,123123,"iron armor")
	print(player)
	save_player(player)
	TopScore()
	input()
