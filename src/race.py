# race.py
from player import Player
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
END = "\033[0m"
race_color={
    "Elf":LIGHT_GREEN,
    "Orc":GREEN,
    "Demon":RED,
    "Human":YELLOW
}
def get_races():
    """Return a list of races and their stats."""
    races = [
        ("Elf", 21, 12, 3, 1),
        ("Orc", 26, 7, 9, 1),
        ("Demon", 20, 18, 2, 1),
        ("Human", 19, 17, 6, 1)
    ]
    return races
def show_skill(player):
    skill_info={
        "Elf":[
            ("Double Arrow","shoot arrow twice to the enemy"),
            ("Sharp Eye","increases chance to do critical damage")
        ],
        "Orc":[
            ("Throw","deals damage without getting hit for 1 turn"),
            ("Heavy Attack","deals 2x damage for 1 turn")
        ],
        "Demon":[
            ("Life Steal","20% of the damage heals you"),
            ("Rage","increases your damage by 1.5x for 1 turn")
        ],
        "Human":[
            ("Triple Slash","deals damage 3 times but all of the attack are halved"),
            ("Rage","increases your damage by 2x for 1 turn")
        ]
    }
    race=player.race
    color=race_color.get(race,"")
    skills=skill_info.get(race,"")
    print(f"{color}{race}{END}\n{'':-<20}")
    for i,(skill,desc)in enumerate(skills,start=1):
        print(f"{i}. {color}{skill}{END}")
    print(f"{'':-<20}")
    print("1.skill information")
    print("2.exit")
    choice=input(">")
    try:
        choice=int(choice)
    except ValueError:
        print("thats not a choice")
    else:
        if choice==1:
            print(f"{'':-<40}")
            for i,(skill,desc)in enumerate(skills,start=1):
                print(f"{color}{skill}{END}\n  {desc}")
            print(f"{'':-<40}")
def show_race():
    """Print available races and their stats nicely."""
    races = get_races()
    for i, (name, hp, strength, defense, _) in enumerate(races,start=1):
        #matching races name with race_color dictionary
        color=race_color.get(name,"")
        print(f"{i}. {color}{name}{END}\n{'':-<20}\nHP: {hp}\nStrength: {strength}\nDefense: {defense}\n{'':-<20}\n")
def race_pick(choice):
    """Return the stats of the selected race as a tuple."""
    races = get_races()
    return races[choice]
		
if __name__=="__main__":
    show_race()
    race,hp,strength,defense,level=race_pick(0)

    player=Player("justin",race,hp,strength,defense,level)
    print(player)
    show_skill(player)
    input()
