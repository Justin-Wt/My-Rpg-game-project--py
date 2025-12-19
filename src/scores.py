from player import Player
File="stats.txt"
def load_player():
	players=[]

	try:
		with open(File,"r") as stats:
			for indexs, rows in enumerate(stats,start=1):
				parts=rows.strip().split(":")
				if len(parts)!=9:
					print(f"skipping corrupted line: {rows}")
					print("error caused because its missing a stats")
					continue
				name,hp,strength,defense,level,weapon,health_potion,mana_potion,armor=parts
				try:
					players.append(Player(name, int(hp), int(strength), int(defense),int(level),weapon,int(health_potion),int(mana_potion),armor))
				except ValueError:
					print(f"[line{indexs}] is skipped because its corrupted line: {rows}")
					print("error caused because one of the variable has a false value")
					continue
	except FileNotFoundError:
		pass 
	return players
def save_player(player):
	players=load_player()
	update=False
	for i, p in enumerate(players):
		if p.name == player.name:
			players[i]=player
			update=True
			break
	if not update:
		players.append(player)
	with open(File, "w") as scor:
		for p in players:
			scor.write(f"{p.name}:{p.hp}:{p.strength}:{p.defense}:{p.level}:{p.weapon}:{p.health_potion}:{p.mana_potion}:{p.armor}\n")
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