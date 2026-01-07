# Imports
import json
import pygame
import sys
import os
import random
from shop import sell_item,shop_items,buy_item
from player import  Player
from enemy import Enemy
from race import  race_pick

#Colors
GREEN_BG       = (0, 180, 0)
DARK_GREEN_BG  = (0, 60, 0)
RED_BG         = (180, 0, 0)
YELLOW_BG      = (180, 180, 0)
GREEN       = (0, 255, 0)
DARK_GREEN  = (0, 120, 0)
RED         = (255, 0, 0)
YELLOW      = (255, 255, 0)
WHITE       = (255, 255, 255)

#font
default_font="assets/fonts/my_font.otf"
# Boot Up
pygame.init()

# Get screen info
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height))
ui_surface = pygame.Surface((width, height))
base_w, base_h = 800, 1200

# Offsets Menu

UI_W,UI_H=int(-0.17*width),0

# Landscape and portrait stabilizer
def update_button_positions():
    new_game_button.rect.topleft = (width // 2 - btn_w // 2 ,rect_h + int(300 * scale))
    load_button.rect.topleft = (width //2 - btn_w // 2 ,rect_h + int(400 * scale))
    start_button.rect.topleft = (width // 2 - btn_w // 2 , rect_h + int(300 * scale))
    quit_button.rect.topleft = (width // 2 - btn_w // 2, rect_h + int(400 * scale))
    attack_button.rect.topleft = (width // 2 - btn_w // 4+UI_W*2, rect_h + int(300 * scale))
    skill_button.rect.topleft  = (width // 2 - btn_w // 4+UI_W*2, rect_h + int(400 * scale))

def handle_gameplay_input(event):
    pass
# Scaling
scale = max(0.75, min(min(width / base_w, height / base_h), 1.2))
btn_w = int(380 * scale)
btn_h = int(60 * scale)
bar_h = int(30 * scale) + UI_H
text_w = width // 2 - int(440 * scale) + UI_W*1.8
rect_w = width // 2 - int(200 * scale // 2)+UI_W*2
rect_h = height // 2 + UI_H
normal_font = pygame.font.Font(None, int(75 * scale))
font = pygame.font.Font(default_font, int(75 * scale))
small_font = pygame.font.Font(default_font, int(65 * scale))
big_font=pygame.font.Font(default_font,int(80*scale))
race_font=pygame.font.Font(default_font,int(160*scale))
# Button class
class Button:
    def _init_(self, x, y, w, h, text, color=(255,255,255), font=pygame.font.Font(default_font, int(75 * scale)),hover_color=(100,100,100),text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center=x,y
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font=font
        self.text_color=text_color
        self.pressed = False
        self.stay_pressed=False
        self.never_pressed=False
    def never_hover(self):
        self.never_pressed=True
    def stay_hover(self):
        self.stay_pressed=True
    def neutralize(self):
        self.stay_pressed=False
        self.never_pressed=False
    def draw(self, surface):
        # Mouse position for PC version later
        mouse_pos = pygame.mouse.get_pos()
        if self.stay_pressed:
            color=self.hover_color
        elif self.never_pressed:
            color=self.color
        elif self.pressed:
            color=self.color
        elif self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color
        pygame.draw.rect(surface, color, self.rect)
        lines = self.text.split("\n")
        line_height = self.font.get_height()
        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, self.text_color)
            text_rect = text_surf.get_rect(center=(self.rect.centerx, self.rect.top + line_height//2 + i*line_height))
            surface.blit(text_surf, text_rect)
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                return True

        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False

        return False

#Inventory
equipment_items=[]
items=[]
def inventory():
    global equipment_items,items
    temporary_equipment_items=[]
    equipment_items=[]
    items=[]
    temporary_equipment_items.extend(player.inventory.weapon)
    temporary_equipment_items.extend(player.inventory.armor)
    temporary_equipment_items.extend(player.inventory.accessories)
    if temporary_equipment_items:
        for item in temporary_equipment_items:
            equipment_items.append(font.render(item,True,WHITE))
    items.append(font.render(f"{'gold':<100}:{player.inventory.gold}",True,(255,255,255)))
    for item,amount in player.inventory.items.items():
        inv_item=f"{item:<100}:{amount:<4}"
        items.append(font.render(inv_item,True,WHITE))
#save files
save_files = ["save_slot1.json", "save_slot2.json", "save_slot3.json","save_slot4.json"]
save_slot=[]
def update_save():
    global save_slot
    save_slot.clear()
    for idx,file_path in enumerate(save_files):
        try:
            with open(file_path,"r")as save:
                files=json.load(save)
                inv=files["inventory"]
                name=files["name"]
                race=files["race"]
                level=files["level"]
                xp=files["xp"]
                hp=files["hp"]
                strs=files["str"]
                defs=files["def"]
                gold=inv["gold"]
                button=Button(
                    x=width//2,
                    y=btn_h*4.5*idx+int(10*idx*scale)+int(150*scale),
                    w=btn_w*3,
                    h=btn_h*5,  
                    text=f"\n{name:<100}level:{level}\n{'':-<100}\nrace:{race:<5}{'':<95}\nhp:{hp:<30}strength:{strs:<30}defense:{defs:<20}\ngold:{gold:<101}\n{'':-<100}",
                    font=pygame.font.Font(default_font,int(40*scale))
                )
                save_slot.append(button)
        except FileNotFoundError:
            btn=Button(
                x=width//2,
                y=btn_h*4.5*idx+int(10*idx*scale)+int(150*scale),
                w=btn_w*3,
                h=btn_h*5, 
                text=f"\n\n\nSave slot {idx+1}",font=pygame.font.Font(default_font,int(40*scale))
                )
            save_slot.append(btn)
        
#Player Status
def get_player_value(player):
    hp=player.hp
    defense=player.defense
    strength=player.strength
    name=player.name
    race=player.race
    level=player.level
    xp=player.xp
    req_xp=5*level+6
    rank=player.rank
    skill1=player.skill1
    skill2=player.skill2
    total_sp=player.total_skill_point
    current_sp=player.current_skill_point
    total_rating=hp+defense+strength
    return [
        f"{name:<16} {race:<10} rank({rank:<2}){'':<10}level:{level}",
        f"{'':-<60}",
        f"xp:{xp}/{req_xp}",
        f"hp:{hp}",
        f"def:{defense}",
        f"str:{strength}",
        f"skill1:{skill1}",
        f"skill2:{skill2}",
        f"total:{total_rating}",
        f"sp:{total_sp}/{current_sp}",
        f"{'':-<60}"]
#Enemy Loot
def enemy_loot():
    drop=enemy.drop_loot()
    loot=[]
    for item in drop:
        stuff,amount=item
        loot.append(f"{stuff}:{amount}")
        player.inventory.add_item(stuff,amount)
    return loot
#shop
def shopping():
    item_list=[]
    for i,(item,price) in enumerate(shop_items,start=1):
        shop_item=Button(
            x=width//2,
            y=height//6*i,
            w=width//4*3,
            h=height//6.1,
            text=f"\n{item:<100}{price}gold",
            color=(0,0,0),
            font=big_font,
            text_color=WHITE,
            hover_color=(175,175,175)
            )
        item_list.append(shop_item)
    return item_list
#selling
def selling():
    sell_list = []
    for i, (item, amount) in enumerate(player.inventory.items.items()):
        if item == "gold":
            continue

        price = next((p for name, p in shop_items if name == item), None)
        if price is None:
            continue

        btn = Button(
            x=width//2,
            y=height//6*(i+1),
            w=width//4*3,
            h=height//7,
            text=f"\n{item:<100}x{amount}  sell:{price//2}g",
            color=(0,0,0),
            font=big_font,
            text_color=WHITE,
            hover_color=(175,175,175)
        )
        sell_list.append((btn, item, price))
    return sell_list
# Buttons
return_button=Button(width//8,height-height//8,btn_w,btn_h,"Return",WHITE)
next_button=Button(width//2,height//2,width,height,"Continue",(0,0,0),hover_color=(0,0,0))
continue_button=Button(width//2,rect_h+int(200*scale),btn_w,btn_h*2,"Continue",WHITE)
yes_button=Button(width//3,rect_h+int(200*scale),btn_w,btn_h*2,"Yes",WHITE)
No_button=Button(width//3*2,rect_h+int(200*scale),btn_w,btn_h*2,"No",WHITE)
new_game_button = Button(width//2, rect_h + int(300 * scale), btn_w, btn_h, "New Game", WHITE)
load_button = Button(width//2, height-height//8,btn_w,btn_h, "Load", WHITE)
start_button = Button(width//2, rect_h + int(300 * scale), btn_w, btn_h, "Start", WHITE)
quit_button = Button(width//2, height-height//8,btn_w,btn_h, "Quit", WHITE)
attack_button = Button(rect_w, rect_h + int(300 * scale), btn_w, btn_h, "Attack", WHITE,font, YELLOW)
skill_button = Button(rect_w, rect_h + int(400 * scale), btn_w, btn_h, "Skill", WHITE,font, YELLOW)
#player stats

atb_surf = font.render("  ATB:", True, (0,150,255))
hp_surf = font.render("   HP:", True, (255,0,0))
skill_surf = font.render("skill:", True, (128,0,128))
#New Game Warning
warning=font.render("Warning:",True,(255,255,255))
warning1=font.render("This action will overwrite",True,(255,255,255))
warning2=font.render("your previous save.",True,(255,255,255))
warning3=font.render("proceed?",True,(255,255,255))
warning_rect=warning.get_rect(center=(width//2,height//8))
warning_rect1=warning1.get_rect(center=(width//2,height//8*1.5))
warning_rect2=warning2.get_rect(center=(width//2,height//4))
warning_rect3=warning3.get_rect(center=(width//2,height//8*2.5))
#Load Warning
load_warning=font.render("Warning:",True,(255,255,255))
load_warning1=font.render("There's no save",True,(255,255,255))
load_warning2=font.render("data ever recorded",True,(255,255,255))
load_warning3=font.render(" Here",True,(255,255,255))
load_warning_rect=load_warning.get_rect(center=(width//2,height//8))
load_warning_rect1=load_warning1.get_rect(center=(width//2,height//8*1.5))
load_warning_rect2=load_warning2.get_rect(center=(width//2,height//4))
load_warning_rect3=load_warning3.get_rect(center=(width//2,height//8*2.5))
#intro
next_surf=font.render("tap to continue",True,(255,255,255))
intro1=big_font.render("you just got reincarnated",True,(255,255,255))
intro2=big_font.render("you found yourself",True,(255,255,255))
intro3=big_font.render("you look at your",True,(255,255,255))
intro1_5=big_font.render("into another world.",True,(255,255,255))
intro2_5=big_font.render("awake in the forest, alone.",True,(255,255,255))
intro3_5=big_font.render("reflection in the water. ",True,(255,255,255))
intro4=big_font.render("you are a...",True,(255,255,255))
next_surf_rect=next_surf.get_rect(center=(width//8*7,height-height//18))
intro1_rect=intro1.get_rect(center=(width//5,height//8))
intro2_rect=intro2.get_rect(center=(width//2,height-height//8*1.5))
intro3_rect=intro3.get_rect(center=(width//5*4,height//8))
intro1_5_rect=intro1_5.get_rect(center=(width//5,height//8*1.5))
intro2_5_rect=intro2_5.get_rect(center=(width//2,height-height//8))
intro3_5_rect=intro3_5.get_rect(center=(width//5*4,height//8*1.5))
intro4_rect=intro4.get_rect(center=(width//2,height//8))
#Races
elf_box=(width//2.75, 75, width//4, rect_h//1.5 )
orc_box=(width//2.75,75,width//4,rect_h//1.5)
demon_box=(width//2.75, 75, width//4, rect_h//1.5 )
human_box=(width//2.75,75,width//4,rect_h//1.5)
elf_button=Button(width//5,height//2,width//5,height,"\n\n\n\n\nElf",(0,0,0),font=race_font,text_color=GREEN)
orc_button=Button(width//5*2,height//2,width//5,height,"\n\n\n\n\nOrc",(0,0,0),font=race_font,text_color=DARK_GREEN)
demon_button=Button(width//5*3,height//2,width//5,height,"\n\n\n\n\nDemon",(0,0,0),font=race_font,text_color=RED)
human_button=Button(width//5*4,height//2,width//5,height,"\n\n\n\n\nHuman",(0,0,0),font=race_font,text_color=YELLOW)
races_surf=race_font.render("you are",True,(255,255,255))
elf_surf=race_font.render(" an Elf",True,GREEN)
orc_surf=race_font.render(" an Orc",True,DARK_GREEN)
demon_surf=race_font.render("a Demon",True,RED)
human_surf=race_font.render("a Human",True,YELLOW)
#Name
name_surf=font.render("What is your name?",True,(255,255,255))
name_surf_rect=name_surf.get_rect(center=(width//2,height//8))
name_button=Button(width//2,height//2,btn_w*1.5,btn_h*3,"\nInput Name...",(50,50,50),hover_color=(100,100,100),text_color=(100,100,100))
ok_button=Button(width//2,height//3*2,btn_w,btn_h,"Ok",(255,255,255),hover_color=(100,100,100),text_color=(0,0,0))
#Main Menu
explore_button=Button(width//7,height//8,btn_w,btn_h*2,"Explore",WHITE)
status_button=Button(width//7,height//8*2,btn_w,btn_h*2,"Status",WHITE)
inventory_button=Button(width//7,height//8*3,btn_w,btn_h*2,"Inventory",WHITE)
save_button=Button(width//7,height//8*4,btn_w,btn_h*2,"Save",WHITE)
loads_button=Button(width//7,height//8*5,btn_w,btn_h*2,"Load",WHITE)
shop_button=Button(width//7,height//8*6,btn_w,btn_h*2,"Shop",WHITE)
exit_button=Button(width//7,height//8*7,btn_w,btn_h*2,"Exit",WHITE)
#Explore
level_required=small_font.render("Lv.10Reccomended",True,(150,150,150))
level_required_surf=level_required.get_rect(center=(width//2,height//8*4.5+25))
explore_surf=font.render("Where do you want to explore?",True,(255,255,255))
explore_surf_rect=explore_surf.get_rect(center=(width//2,height//8))
forest_button=Button(width//2,height//8*3.5,btn_w,btn_h*2,"Forest",WHITE)
cave_button=Button(width//2,height//8*4.5,btn_w,btn_h*2,"Cave",WHITE)
#Inventory
inventory_surf=big_font.render("Inventory",True,(255,255,255))
inventory_surf_rect=inventory_surf.get_rect(center=(width//2,height//8))
Equipment_button=Button(width//3,height-height//8-btn_h,btn_w,btn_h,"Equipment",WHITE)
Item_button=Button(width//3*2,height-height//8-btn_h,btn_w,btn_h,"Item",WHITE)
next_inv_button=Button(width-width//4,height-height//8,btn_w//3,btn_h,"->",WHITE)
previous_inv_button=Button(width-width//4-btn_w-5,height-height//8,btn_w//3,btn_h,"<-",WHITE)

#Quit
main_menu_button=Button(width//2,height//2-btn_h*4,width//4,btn_h*2,"quit to main menu",WHITE)
quitting_button=Button(width//2,height//2,width//4,btn_h*2,"quit the game",WHITE)
close_button=Button (width//2,height//2+btn_h*4,width//4,btn_h*2,"close",WHITE)

#Win and Lose
looted_surf=big_font.render("you got",True,WHITE)
looted_surf_rect=looted_surf.get_rect(center=(width//2,height//4))
win_surf=race_font.render("You Win",True,WHITE)
win_surf_rect=win_surf.get_rect(center=(width//2,height//8))
lose_surf=[
    (
        race_font.render("the enemy use:",True,WHITE),
        race_font.render("reality check",True,WHITE),
        race_font.render("its very effective.",True,WHITE)
    ),
    (
        race_font.render("knock knock",True,WHITE),
        race_font.render("its your skill",True,WHITE),
        race_font.render("oh wait,",True,WHITE),
        race_font.render("you don't have any skill",True,WHITE)
    ),
    (
        race_font.render("it's a bird",True,WHITE),
        race_font.render("it's a plane",True,WHITE),
        race_font.render("its a...",True,WHITE),
        race_font.render("Loser",True,WHITE)
    ),
    (
        race_font.render("dont be sad",True,WHITE),
        race_font.render("it's normal to fail...",True,WHITE),
        race_font.render("for someone like you.",True,WHITE),
        race_font.render("Loser",True,WHITE)
    ),
    (
        race_font.render("remember i will:",True,WHITE),
        race_font.render("never gonna give you up",True,WHITE),
        race_font.render("never gonna let you down",True,WHITE)
    )
]
#Shop
back_button=Button(width//3,height//2+btn_h*2.5,width//16,btn_h,"Cancel",WHITE)
main_shop=font.render("Welcome to the shop!",True,WHITE)
main_shop1=font.render("what would you like to do?",True,WHITE)
main_shop_rect=main_shop.get_rect(center=(width//2,height//8))
main_shop1_rect=main_shop1.get_rect(center=(width//2,height//4))
buy_button=Button(width//3,height-height//3,width//8,btn_h,"Buy",WHITE)
sell_button=Button(width-width//3,height-height//3,width//8,btn_h,"Sell",WHITE)
add_button=Button (width-width//3,height//2-btn_h,width//32,height//32,"^",WHITE)
buying=Button(width-width//3,height//2+btn_h*2.5,width//16,btn_h,"Ok",WHITE)
decrease_button=Button (width-width//3,height//2+btn_h,width//32,height//32,"v",WHITE,font=normal_font)
#Time and cooldown
atb = 0
fps_timer = 0
speed = 120
cast_time = 0
clock = pygame.time.Clock()
pygame.display.set_caption("My First Pygame")

# Text input
text = ""
text_surface = font.render(text, True, (255,255,255))

#States
STATE_START = 0
STATE_SAVES = 1
STATE_NEW_GAME = 2
STATE_INTRO = 3
STATE_NAME = 4
STATE_LOAD = 5
STATE_FIGHT = 6
STATE_MAIN_MENU=7
STATE_EXPLORE=8
STATE_INVENTORY=9
STATE_SAVE=10
STATE_STATUS=11
STATE_SHOP=12
STATE_EXIT=13
STATE_LOSE=14
STATE_WIN=15
STATE_BUY=16
STATE_SELL=17
STATE_LOAD_GAME=18
state = STATE_START
#variables
intro=0
dims=0
dimmer=0
xp=0
total=1
total_price=0
decreasing=False
adding=True
how_much=False
clickable=False
skill_ui=False
show_name_ui=False
show_picks=False
show_load_warning = False
show_new_game_warning = False
choice=False
atb_ratio=0
enemy_atb_ratio=0
hp_ratio=1
fps_surf = font.render("0", True, (RED))
running = True
item_picked=None
box=None
color=None
choice_button=None
button1=None
button2=None
button3=None
refresh_inventory=True
inventory_mode=None
#Drawing
def draw_start():
    start_button.draw(ui_surface)
    quit_button.draw(ui_surface)
    
def draw_saves():
    new_game_button.draw(ui_surface)
    load_button.draw(ui_surface)
    
def draw_new_game():
    update_save()
    
    for slots in save_slot:
        slots.draw(ui_surface)
    return_button.draw(ui_surface)
    if show_new_game_warning:
        dim_overlay = pygame.Surface((width, height))
        dim_overlay.set_alpha(150)   # 0 = invisible, 255 = fully black
        ui_surface.blit(dim_overlay,(0,0))
        pygame.draw.rect(ui_surface,(50,50,50),(width//3,height//10,width//3,rect_h//2))
        ui_surface.blit(warning,warning_rect)
        ui_surface.blit(warning1,warning_rect1)
        ui_surface.blit(warning2,warning_rect2)
        ui_surface.blit(warning3,warning_rect3)
        yes_button.draw(ui_surface)
        No_button.draw(ui_surface)
        
def draw_intro():
    next_button.draw(ui_surface)
    ui_surface.blit(intro1,intro1_rect)
    ui_surface.blit(intro1_5,intro1_5_rect)
    ui_surface.blit(next_surf,next_surf_rect)
    if intro>=1:
        ui_surface.blit(intro2,intro2_rect)
        ui_surface.blit(intro2_5,intro2_5_rect)
    if intro>=2:
        ui_surface.blit(intro3,intro3_rect)
        ui_surface.blit(intro3_5,intro3_5_rect)
               
def draw_name():
        if not show_name_ui: 
            elf_button.draw(ui_surface)
            orc_button.draw(ui_surface)
            demon_button.draw(ui_surface)
            human_button.draw(ui_surface)
            ui_surface.blit(intro4,intro4_rect)
        if show_picks and not show_name_ui:
            dim_overlay = pygame.Surface((width, height))
            dim_overlay.set_alpha(100)  # 0 = invisible, 255 = fully black
            ui_surface.blit(dim_overlay,(0,0))
            choice_button.stay_hover()
            button1.never_hover()
            button2.never_hover()
            button3.never_hover()
            pygame.draw.rect(ui_surface,color,box)
            ui_surface.blit(races_surf,(width//2.5,100,rect_w,rect_h))
            ui_surface.blit(race_text,(width//2.5,250,rect_w,rect_h))
            yes_button.draw(ui_surface)
            No_button.draw(ui_surface)
        if show_name_ui:
            ui_surface.blit(name_surf,name_surf_rect)
            name_button.draw(ui_surface)
            text_surface = font.render(text, True, (255,255,255))
            ui_surface.blit(text_surface, (width//2-rect_w, height//2))
            ok_button.draw(ui_surface)

def draw_load():
    update_save()
    return_button.draw(ui_surface)
    for slots in save_slot:
        slots.draw(ui_surface)
    if show_load_warning:
        dim_overlay = pygame.Surface((width, height))
        dim_overlay.set_alpha(150)   # 0 = invisible, 255 = fully black
        ui_surface.blit(dim_overlay,(0,0))
        pygame.draw.rect(ui_surface,(50,50,50),(width//3,height//10,width//3,rect_h//2))
        ui_surface.blit(load_warning,load_warning_rect)
        ui_surface.blit(load_warning1,load_warning_rect1)
        ui_surface.blit(load_warning2,load_warning_rect2)
        ui_surface.blit(load_warning3,load_warning_rect3)
        continue_button.draw(ui_surface)

def draw_fight():
    global fps_timer,fps_surf
    total_surf=font.render(f"{total_hp}/{player.hp}",True,RED)
    total_enemy_hp_surf=font.render(f"{total_enemy_hp}/{enemy.hp}",True,(255,255,255))
    enemy_name=font.render(enemy.name,True,WHITE)
    text_surface = font.render(text, True, (255,255,255))
    pygame.draw.rect(ui_surface, (100,100,100), (0, rect_h, width, height))
    if fps_timer >= 0.2:
        fps_surf = font.render(f"FPS:{int(clock.get_fps())}", True, (255,255,255))
        fps_timer = 0
    pygame.draw.rect(ui_surface, (50,50,50), (width//8, height//2+btn_h*2.2, rect_w*2, bar_h))
    pygame.draw.rect(ui_surface, (0,150,255), (width//8, height//2+btn_h*2.2, atb_ratio*rect_w*2, bar_h))
    ui_surface.blit(text_surface,(width//16,height//2-btn_h))
    ui_surface.blit(total_surf,(width//8,height//2+btn_h*1.1))
    ui_surface.blit(fps_surf, (0,0))
    ui_surface.blit(hp_surf, (width//16, height//2+btn_h))
    ui_surface.blit(atb_surf, (width-width//16-rect_w*2-width//8-int(40*scale), height//2+btn_h*2))
    ui_surface.blit(hp_surf, (width-width//16-rect_w*2-width//8, height//2+btn_h))
    ui_surface.blit(atb_surf, (width//16-int(40*scale), height//2+btn_h*2))
    ui_surface.blit(enemy_name,(width-width//16-rect_w*2-width//8,height//2-btn_h))
    ui_surface.blit(total_enemy_hp_surf,(width-width//8-rect_w*2,height//2+btn_h*1.1))
    pygame.draw.rect(ui_surface,(50,50,50),(width-width//8-rect_w*2,height//2+btn_h*2.2, rect_w*2, bar_h))
    pygame.draw.rect(ui_surface,(0,150,255),(width-width//8-rect_w*2,height//2+btn_h*2.2, enemy_atb_ratio*rect_w*2, bar_h))
    
    if player.atb >= 100:
        attack_button.draw(ui_surface)
        skill_button.draw(ui_surface)

def draw_main_menu():
    explore_button.draw(ui_surface)
    status_button.draw(ui_surface)
    inventory_button.draw(ui_surface)
    save_button.draw(ui_surface)
    loads_button.draw(ui_surface)
    shop_button.draw(ui_surface)
    exit_button.draw(ui_surface)

def draw_explore():
    ui_surface.blit(explore_surf,(explore_surf_rect))
    forest_button.draw(ui_surface)
    cave_button.draw(ui_surface)
    if player.level<10:
        ui_surface.blit(level_required,level_required_surf)

def draw_inventory():
    ui_surface.blit(inventory_surf,inventory_surf_rect)
    if not inventory_mode:
        Equipment_button.draw(ui_surface)
        Item_button.draw(ui_surface)
        quit_button.draw(ui_surface)
    if inventory_mode=="equipment":
        current_equipment_page=1
        next_inv_button.draw(ui_surface)
        equipment_pages=0
        for i,item in enumerate(equipment_items,start=1):
            ui_surface.blit(item,(width//5*2,height//16*(i+2),width//3,height//8))
            equipment_pages=i//10
        equipment_page_surf =font.render(f"{current_equipment_page}/{equipment_pages+1}",True,WHITE)
        equipment_page_surf_rect=equipment_page_surf.get_rect(center=(width//2,height-height//8))
        ui_surface.blit(equipment_page_surf,equipment_page_surf_rect)
        next_inv_button.draw(ui_surface)
        previous_inv_button.draw(ui_surface)
        return_button.draw(ui_surface)
    if inventory_mode=="item":
        current_item_page=1
        for i,item in enumerate(items,start=1):
            ui_surface.blit(item,(width//8,height//16*(i+2),width//3,btn_h))
            item_pages=i//10
        item_page_surf =font.render(f"{current_item_page}/{item_pages+1}",True,WHITE)
        item_page_surf_rect=item_page_surf.get_rect(center=(width//2,height-height//8))
        ui_surface.blit(item_page_surf,item_page_surf_rect)
        next_inv_button.draw(ui_surface)
        previous_inv_button.draw(ui_surface)
        return_button.draw(ui_surface)

def draw_status():
    stat=get_player_value(player)
    quit_button.draw(ui_surface)
    for i,value in enumerate(stat):
        stats=font.render(value,True,WHITE)
        ui_surface.blit(stats,(width//4,height//16*i+btn_h))
def draw_win(dims,player_loot,xp):
    dims+=5
    if dims>=255:
        dims=255
        next_button.draw(ui_surface)
        ui_surface.blit(next_surf,next_surf_rect)
        ui_surface.blit(looted_surf,looted_surf_rect)
        for i,item in enumerate(player_loot,start=1):
            myitem=big_font.render(item,True,WHITE)
            myitem.set_alpha(dims)
            ui_surface.blit(myitem,(width//3,height//8*(i+2)))
        xp_surf=font.render(f"you got {xp}exp",True,WHITE)
        ui_surface.blit(xp_surf,(width//3,height-height//8))
    win_surf.set_alpha(dims)
    ui_surface.blit(win_surf,win_surf_rect)
    return dims
def draw_lose(dims,lose_message):
    dims+=5
    if dims>=255:
        dims=255
        next_button.draw(ui_surface)
        ui_surface.blit(next_surf,next_surf_rect)
    for i, lines in enumerate(lose_message,start=1):
        line_rect=lines.get_rect(center=(width//2,height//8*(i+1)))
        lines.set_alpha(dims)
        ui_surface.blit(lines,line_rect)
    return dims
def draw_exit():
    main_menu_button.draw(ui_surface)
    quitting_button.draw(ui_surface)
    close_button.draw(ui_surface)
def draw_shop():
    ui_surface.blit(main_shop,main_shop_rect)
    ui_surface.blit(main_shop1,main_shop1_rect)
    buy_button.draw(ui_surface)
    sell_button.draw(ui_surface)
    quit_button.draw(ui_surface)
def draw_sell(lists,price,amount,item):
    pygame.draw.rect(ui_surface,(100,100,100),(width//8,height//12-5,width-width//8,height-height//3+10))
    return_button.draw(ui_surface)
    for item,, in lists:
        item.draw(ui_surface)
    if how_much:
        dim_overlay = pygame.Surface((width, height))
        dim_overlay.set_alpha(150)
        ui_surface.blit(dim_overlay,(0,0))
        back_button.draw(ui_surface)
        pygame.draw.rect(ui_surface,WHITE,(width-width//3-width//64-3,height//2-btn_h//2-3,width//32+6,btn_h+6))
        pygame.draw.rect(ui_surface,WHITE,(width-width//3-width//64,height//2-btn_h//2,width//32,btn_h))
        item_surf=big_font.render(f"{item_picked}",True,(0,0,0))
        item_surf_rect=item_surf.get_rect(centery=height//2)
        price_surface=font.render(f"{total}",True,(0,0,0))
        total_surface=font.render(f"{amount}",True,(0,0,0))
        pygame.draw.rect(ui_surface,WHITE,(width//2-btn_w//2,height//2+btn_h*2,btn_w,btn_h))
        price_surface_rect=price_surface.get_rect(center=(width//2,height//2+btn_h*2+int(40*scale)))
        total_surface_rect=total_surface.get_rect(center=(width-width//3,height//2))
        pygame.draw.rect(ui_surface,WHITE,(width//2-width//6,height//2-btn_h,width//3.5,btn_h*2))
        ui_surface.blit(item_surf,(width//3,item_surf_rect.y))
        
        ui_surface.blit(price_surface,price_surface_rect)
        ui_surface.blit(total_surface,total_surface_rect)
        buying.draw(ui_surface)
        if adding:
            add_button.draw(ui_surface)
        if decreasing:
            decrease_button.draw(ui_surface)
def draw_buy(lists,total,amount,item_picked):
    pygame.draw.rect(ui_surface,(100,100,100),(width//8,height//12-5,width-width//8,height-height//3+10))
    return_button.draw(ui_surface)
    for item in lists:
        item.draw(ui_surface)
    if how_much:
        dim_overlay = pygame.Surface((width, height))
        dim_overlay.set_alpha(150)
        ui_surface.blit(dim_overlay,(0,0))
        back_button.draw(ui_surface)
        pygame.draw.rect(ui_surface,WHITE,(width-width//3-width//64-3,height//2-btn_h//2-3,width//32+6,btn_h+6))
        pygame.draw.rect(ui_surface,WHITE,(width-width//3-width//64,height//2-btn_h//2,width//32,btn_h))
        item_surf=big_font.render(f"{item_picked}",True,(0,0,0))
        item_surf_rect=item_surf.get_rect(centery=height//2)
        price_surface=font.render(f"{total}",True,(0,0,0))
        total_surface=font.render(f"{amount}",True,(0,0,0))
        pygame.draw.rect(ui_surface,WHITE,(width//2-btn_w//2,height//2+btn_h*2,btn_w,btn_h))
        price_surface_rect=price_surface.get_rect(center=(width//2,height//2+btn_h*2+int(40*scale)))
        total_surface_rect=total_surface.get_rect(center=(width-width//3,height//2))
        pygame.draw.rect(ui_surface,WHITE,(width//2-width//6,height//2-btn_h,width//3.5,btn_h*2))
        ui_surface.blit(item_surf,(width//3,item_surf_rect.y))
        
        ui_surface.blit(price_surface,price_surface_rect)
        ui_surface.blit(total_surface,total_surface_rect)
        buying.draw(ui_surface)
        if adding:
            add_button.draw(ui_surface)
        if decreasing:
            decrease_button.draw(ui_surface)
# Main loop
while running:
    player_shop_list=shopping()
    if state == STATE_BUY:
        if total>1:
            decreasing=True
        else:
            decreasing=False
    if state == STATE_SELL:
        if total>1:
            decreasing=True
        else:
            decreasing=False
    # Time and FPS handler
    dt = clock.tick(60) / 1000
    fps_timer += dt
    if state==STATE_FIGHT:
        enemy.update_atb(dt)
        player.update_atb(dt)
        player.update_action(dt,enemy)
        atb_ratio=player.atb/100
        enemy_atb_ratio=enemy.atb/100
        if enemy.atb>=100:
            enemy.attack(player)
            total_surf=font.render(f"{total_hp}/{player.hp}",True,RED)
            enemy.atb=0
        if player.hp<=0:
            lose_message=random.choice(lose_surf)
            state=STATE_LOSE
        elif enemy.hp<=0:
            player_loot=enemy_loot()
            state=STATE_WIN
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Start menu button handling
        if state == STATE_START:
            if start_button.handle_event(event):
                
                state = STATE_SAVES
                pygame.event.clear()
            elif quit_button.handle_event(event):
                running = False
        elif state == STATE_SAVES:
            if new_game_button.handle_event(event):
                update_save()
                state = STATE_NEW_GAME
                pygame.event.clear()
            elif load_button.handle_event(event):
                update_save()
                state = STATE_LOAD
                pygame.event.clear()
        elif state == STATE_NEW_GAME :
            if not show_new_game_warning:
                for i,slot in enumerate(save_slot):
                    if slot.handle_event(event):
                        selected_save_index=i
                        save_file=f"save_slot{i+1}.json"
                        if os.path.exists(save_file):
                            show_new_game_warning=True
                        
                        else:
                            state=STATE_INTRO 
                if return_button.handle_event(event):
                    state=STATE_SAVES
            elif show_new_game_warning:
                if yes_button.handle_event(event):
                    save_file=f"save_slot{selected_save_index+1}.json"
                    show_new_game_warning = False
                    state=STATE_INTRO
                    pygame.event.clear()
                elif No_button.handle_event(event):
                    show_new_game_warning = False
                    selected_save_index = None
                    pygame.event.clear()
        elif state == STATE_INTRO:
            if next_button.handle_event(event):
                intro+=1
                pygame.event.clear()
                if intro>2:
                    state=STATE_NAME
                    pygame.event.clear()
        elif state == STATE_NAME:
            if not show_picks:
                if elf_button.handle_event(event):
                    choice_button=elf_button
                    choice=0
                    button1=orc_button
                    button2=demon_button
                    button3=human_button
                    box=elf_box
                    color=GREEN_BG
                    race_text=elf_surf
                    show_picks=True
                    pygame.event.clear()
                elif orc_button.handle_event(event):
                    choice_button=orc_button
                    choice=1
                    button1=elf_button
                    button2=demon_button
                    button3=human_button
                    box=orc_box
                    race_text=orc_surf
                    color=DARK_GREEN_BG
                    show_picks=True
                    pygame.event.clear()
                elif demon_button.handle_event(event):
                    choice_button=demon_button
                    choice=2
                    button1=elf_button
                    button2=orc_button
                    button3=human_button
                    box=demon_box
                    race_text=demon_surf
                    color=RED_BG
                    show_picks=True
                    pygame.event.clear()
                elif human_button.handle_event(event):
                    choice_button=human_button
                    choice=3
                    button1=elf_button
                    button2=orc_button
                    button3=demon_button
                    box=human_box
                    race_text=human_surf
                    color=YELLOW_BG
                    show_picks=True
                    pygame.event.clear()
            elif No_button.handle_event(event):
                choice_button.neutralize()
                button1.neutralize()
                button2.neutralize()
                button3.neutralize()
                show_picks=False
                pygame.event.clear()
            elif yes_button.handle_event(event):
                race,hp,defense,strength,skill1,skill2=race_pick(choice)
                show_picks=False
                show_name_ui=True
                break
            if ok_button.handle_event(event):
                if len(text)>3:
                    name=text
                else:
                    name="Hero"
                    text="Hero"
                
                player=Player(name,race,hp,defense,strength,skill1=skill1,skill2=skill2)
                save_file=f"save_slot{selected_save_index+1}.json"
                player.save(save_file)
                total_hp=player.hp
                state=STATE_MAIN_MENU
                pygame.event.clear()
            if name_button.handle_event(event):
                pygame.key.start_text_input()
        elif state == STATE_SHOP:
            if quit_button.handle_event(event):
                state=STATE_MAIN_MENU
            elif buy_button.handle_event(event):
                state=STATE_BUY
                pygame.event.clear
            elif sell_button.handle_event(event):
                state=STATE_SELL
                pygame.event.clear()
        elif state == STATE_SELL:
            sell_list=selling()
            if not how_much:
                if return_button.handle_event(event):
                    state=STATE_MAIN_MENU
                for button,item, price in sell_list:
                    if  button.handle_event(event):
                        item_picked=item
                        selected_price=price
                        total=1
                        how_much=True
            if how_much:
                if back_button.handle_event(event):
                    how_much=False
                item_owned=player.inventory.items.get(item_picked,0)
                if adding:
                    if add_button.handle_event(event):
                        total+=1
                        if total+1>item_owned:
                            adding=False
                if decreasing:
                    if decrease_button.handle_event(event):
                        total-=1
                if buying.handle_event(event):
                    sell_item(player,item_picked,selected_price,total)
                    adding=True
                    how_much=False
                    state=STATE_MAIN_MENU
        elif state == STATE_BUY:
            if not how_much:
                if return_button.handle_event(event):
                    state=STATE_MAIN_MENU
                for i,button in enumerate(player_shop_list):
                    if button.handle_event(event):
                        item_selected=i
                        how_much=True
                        item,selected_price=shop_items[item_selected]
                        item_picked=item
                        total_price=selected_price
                        if player.inventory.gold<total_price+selected_price:
                            adding=False
            if how_much:
                if back_button.handle_event(event):
                    how_much=False
                if adding:
                    if add_button.handle_event(event):
                        total+=1
                        total_price=selected_price*total
                    if player.inventory.gold<total_price+selected_price:
                        adding=False
                elif decreasing:
                    if decrease_button.handle_event(event):
                        total-=1
                        total_price=selected_price*total
                        if player.inventory.gold>total_price:
                            adding=True
                if buying.handle_event(event):
                    buy_item(player,item,selected_price,total)
                    how_much=False
                    state=STATE_MAIN_MENU
        elif state == STATE_SAVE:
            if not show_new_game_warning:
                update_save()
                for i,slot in enumerate(save_slot):
                    if slot.handle_event(event):
                        selected_save_index=i
                        save_file=f"save_slot{i+1}.json"
                        if os.path.exists(save_file):
                            show_new_game_warning=True
                            
                        else:
                            player.save(save_file)
                            state=STATE_MAIN_MENU
                if return_button.handle_event(event):
                    state=STATE_MAIN_MENU
            elif show_new_game_warning:
                if yes_button.handle_event(event):
                    save_file=f"save_slot{selected_save_index+1}.json"
                    player.save(save_file)
                    show_new_game_warning = False
                    state=STATE_MAIN_MENU
                    pygame.event.clear()
                elif No_button.handle_event(event):
                    show_new_game_warning = False
                    selected_save_index = None
                    pygame.event.clear()
            
        elif state == STATE_MAIN_MENU:
            name_surf= font.render(f"{player.name:<16} lvl.{player.level}",True,(255,255,255))
            total_hp=player.hp
            if explore_button.handle_event(event):
                state=STATE_EXPLORE
            elif status_button.handle_event(event):
                state=STATE_STATUS
            elif save_button.handle_event(event):
                update_save()
                state=STATE_SAVE
            elif loads_button.handle_event(event):
                update_save()
                state=STATE_LOAD_GAME
            elif shop_button.handle_event(event):
                state=STATE_SHOP
            elif inventory_button.handle_event(event):
                state=STATE_INVENTORY
            elif exit_button.handle_event(event):
                state=STATE_EXIT
        elif state == STATE_STATUS:
            if quit_button.handle_event(event):
                state=STATE_MAIN_MENU
        elif state == STATE_EXPLORE:
            types=["normal","elite","boss"]
            if forest_button.handle_event(event):
                type=random.choice(types)
                enemy=Enemy.from_area("forest",type)
                total_enemy_hp=enemy.hp
                state=STATE_FIGHT
            elif cave_button.handle_event(event):
                type=random.choice(types)
                enemy=Enemy.from_area("cave",type)
                total_enemy_hp=enemy.hp
                state=STATE_FIGHT
        elif state == STATE_WIN and clickable:
            if next_button.handle_event(event):
                dims=0
                xp=enemy.get_exp()
                player.add_xp(xp)
                player.hp=total_hp
                player.atb=0
                state=STATE_MAIN_MENU
                clickable=False
        elif state == STATE_LOSE and clickable:
            if next_button.handle_event(event):
                dimmer=0
                player.hp=total_hp
                player.atb=0
                state=STATE_MAIN_MENU
                clickable=False
        elif state == STATE_EXIT:
            if main_menu_button.handle_event(event):
                state=STATE_START
            if quitting_button.handle_event(event):
                running=False
            if close_button.handle_event(event):
                state=STATE_MAIN_MENU
        elif state == STATE_INVENTORY:
            if inventory_mode==None:
                if Equipment_button.handle_event(event):
                    inventory_mode="equipment"
                    refresh_inventory=True
                elif Item_button.handle_event(event):
                    inventory_mode="item"
                    refresh_inventory=True
                elif quit_button.handle_event(event):
                    state=STATE_MAIN_MENU
            elif refresh_inventory:
                inventory()
                refresh_inventory=False
            elif return_button.handle_event(event):
                inventory_mode=None
        elif state == STATE_LOAD_GAME:
            if not show_load_warning:
                for i,slot in enumerate(save_slot):
                    if slot.handle_event(event):
                        selected_save_index=i
                        save_file=f"save_slot{i+1}.json"
                        if os.path.exists(save_file):
                            player=Player.load(save_file)
                            text=player.name
                            player.atb=0
                            state=STATE_MAIN_MENU
                            pygame.event.clear()
                        else:
                            show_load_warning=True
                            pygame.event.clear()
                if return_button.handle_event(event):
                    state=STATE_MAIN_MENU
            elif show_load_warning:
                if continue_button.handle_event(event):
                    show_load_warning=False
                    
        elif state == STATE_LOAD:
            if not show_load_warning:
                for i,slot in enumerate(save_slot):
                    if slot.handle_event(event):
                        selected_save_index=i
                        save_file=f"save_slot{i+1}.json"
                        if os.path.exists(save_file):
                            player=Player.load(save_file)
                            text=player.name
                            player.atb=0
                            state=STATE_MAIN_MENU
                            pygame.event.clear()
                        else:
                            show_load_warning=True
                            pygame.event.clear()
                if return_button.handle_event(event):
                    state=STATE_SAVES
            elif show_load_warning:
                if continue_button.handle_event(event):
                    show_load_warning=False
        # Text input
        if event.type == pygame.TEXTINPUT:
            text += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
        # ATB button handling
        if state==STATE_FIGHT:
            if player.atb >= 100:
                if attack_button.handle_event(event) and not skill_ui:
                    player.action_selected="Attack"
                    player.update_action(dt,enemy)
                    print("attack")
                
                elif skill_button.handle_event(event) and not skill_ui:
                    #skill_ui=True
                    pass
                    

    # Drawing
    ui_surface.fill((0, 0, 0))
    if state == STATE_START:
        draw_start()
    elif state == STATE_SAVES:
        draw_saves()
    elif state == STATE_NEW_GAME:
        draw_new_game()
    elif state == STATE_INTRO:
        draw_intro()
    elif state == STATE_NAME:
        draw_name()
    elif state == STATE_LOAD:
        draw_load()
    elif state == STATE_MAIN_MENU:
        draw_main_menu()
    elif state == STATE_FIGHT:
        draw_fight()
    elif state == STATE_EXPLORE:
        draw_explore()
    elif state == STATE_STATUS:
        draw_status()
    elif state == STATE_SAVE:
        draw_new_game()
    elif state == STATE_SHOP:
        draw_shop()
    elif state == STATE_BUY:
        draw_buy(player_shop_list,total_price,total,item_picked)
    elif state == STATE_SELL:
        draw_sell(sell_list,price,total,item_picked)
    elif state == STATE_INVENTORY:
        draw_inventory()
    elif state == STATE_STATUS:
        draw_status()
    elif state == STATE_EXIT:
        draw_exit()
    elif state == STATE_LOAD_GAME:
        draw_load()
    elif state == STATE_WIN:
        dims=draw_win(dims,player_loot,xp)
        if dims>=255:
            clickable=True
    elif state == STATE_LOSE:
        dimmer=draw_lose(dimmer,lose_message)
        if dimmer>=255:
            clickable=True
    screen.fill((0,0,0))
    screen.blit(ui_surface, (0,0))
    pygame.display.flip()

pygame.quit()
sys.exit()
