import time
high_score=0
top_name=""
score_top=[]
class Player:
	def __init__(self,name,score=0):
		self.name=name
		self.score=score

	def add_score(self,points):
		self.score+=points
	def save_scores(self):
		with open("scores.txt", "a") as scor:
			scor.write(f"{self.name}:{self.score}\n")
	def __str__(self):
		return f"{self.name} has {self.score} points"
def add():
	name=input("Enter the player name: ")
	try:
		points=int(input("Enter score:"))
	except ValueError:
		print("your score have to be a number")
	else:
		player=Player(name)
		player.add_score(points)
		player.save_scores()
		print(f"{name}'s score is added")
def view():
	try:
		with open("scores.txt","r") as scor:
			lines=scor.readlines()
			for line in lines:
				name, score=line.strip().split(":")
				score=int(score)
				global high_score, top_name
				if score>high_score:
					high_score=score
					top_name=name
					score_top.insert(0,f"{top_name}:{high_score}")
					print(score_top)
				else:
					score_top.append(f"{name}:{score}")
				player=Player(name,int(score))
				print(player)
	except FileNotFoundError:
		print("No scores file is found")
def exit():
	print("exiting in 5 seconds")
	for count in range(5,0,-1):
		print(count)
		time.sleep(1)
def reset():
	open("scores.txt", "w")
	print("your player has been removed!")
def show_best():
	print("here is the top 5 most scores")
	for idx,name in enumerate(score_top, start=1):
		print(f"{idx}. {name}")
		if idx==5:
			break

def main():
	while True:
		print("====Score Tracker====")
		print("1. Add a new player")
		print("2. View all scores")
		print("3. Show best")
		print("4. Reset score")
		print("5. Exit")
		choice= input("choose an option")
		try:
			choice=int(choice)
		except ValueError:
			print("thats not a number")
		if choice>5 or choice<1:
			print("your option is out of range")
		else:
			if choice==1:
				add()
			elif choice==2:
				view()
			elif choice==3:
				show_best()
			elif choice==4:
				reset()
			elif choice==5:
				exit()
				break
				
main()
