#Imports
import pygame
import sys

#Boot Up
pygame.init()

# get screen info
info=pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height))
ui_surface=pygame.Surface((width, height),pygame.SRCALPHA)
base_w=800
base_h=1200

#Off-Sets Menu
UI_W=-400
UI_H=0

#landscape and potrait stabilizer
def update_button_positions():
    attack_button.rect.topleft = (width//2 - btn_w//2 + UI_W, rect_h + int(300*scale))
    skill_button.rect.topleft  = (width//2 - btn_w//2 + UI_W, rect_h + int(400*scale))

#Button Codes
class Button:
    def __init__(self,x,y,w,h,text,color="gray",hover_color=(100,100,100)):
        self.rect=pygame.Rect(x,y,w,h)
        self.text=text
        self.color=color
        self.hover_color=hover_color
        self.clicked=False
    def draw(self,surface,is_selected=False):
        if is_selected:
            color=self.hover_color
        else:
            color=self.color
        #Mouse_pos for pc-version later
        mouse_pos=pygame.mouse.get_pos()
        ui_mouse=(
            mouse_pos[0]-UI_W,
            mouse_pos[1]-UI_H)
        pygame.draw.rect(surface,color,self.rect)
        text_surf=font.render(self.text,True,(0,0,0))
        text_rect=text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf,text_rect)
        
    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

#Scaling
scale=max(0.75,min(min(width/base_w,height/base_h),1.2))
btn_w=int(380*scale)
btn_h=int(60*scale)
bar_h=int(30*scale)+UI_H
text_w=width//2-(int(440*scale))+UI_W
rect_w=width//2-(int(380*scale)//2)+UI_W
rect_h=height//2+UI_H
font=pygame.font.Font(None,int(100*scale))

#Buttons
attack_button=Button(rect_w,rect_h+int(300*scale),btn_w,btn_h,"Attack",("white"),("yellow"))
skill_button=Button(rect_w,rect_h+int(400*scale),btn_w,btn_h,"Skill",("white"),("yellow"))
update_button_positions()

#Time and Cooldown
atb=0
speed=120
cast_time=0
clock = pygame.time.Clock()
pygame.display.set_caption("My First Pygame")

# Main loop
action_selected=None
running=True
while running:
    #Logic handler
    dt=clock.tick(60)/1000
    if action_selected=="Skill":
        atb=0
        cast_time+=speed/6*dt
        if cast_time>100:
            cast_time=0
            action_selected=None
    if action_selected is None:
        atb+=speed*dt
        if atb>=100:
            atb=100
        
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width,height=event.w,event.h
            ui_surface=pygame.Surface((width, height),pygame.SRCALPHA)
            scale=max(0.75,min(min(width/base_w,height/base_h),1.2))
            btn_w=int(380*scale)
            btn_h=int(60*scale)
            font=pygame.font.Font(None,int(100*scale))
            update_button_positions()
        if atb==100:
            if attack_button.handle_event(event):
                if action_selected=="Attack":
                    print("attack")
                    atb=0
                    action_selected=None
                else:
                    action_selected="Attack"
            elif skill_button.handle_event(event):
                if action_selected=="Skill":
                    print("skill")
                    
                else:
                    action_selected="Skill"

    #drawing
    ui_surface.fill((0, 0, 0,0))
    pygame.draw.rect(ui_surface,(100,100,100),(0,rect_h,width,height))
    ui_surface.blit(font.render("  ATB:",True,(0,150,255)),(text_w,rect_h+int(100*scale)))
    pygame.draw.rect(ui_surface,(50,50,50),(rect_w,rect_h+int(125*scale),btn_w,bar_h))
    ui_surface.blit(font.render("   HP:",True,("red")),(text_w,rect_h+int(200*scale)))
    pygame.draw.rect(ui_surface,("red"),(rect_w,rect_h+int(225*scale),btn_w,bar_h))
    pygame.draw.rect(ui_surface,(0,150,255),(rect_w,rect_h+int(125*scale),atb*btn_w/100,bar_h))
    if atb==100:
        attack_button.draw(ui_surface,is_selected=(action_selected=="Attack"))
        skill_button.draw(ui_surface,is_selected=(action_selected=="Skill"))
    if action_selected=="Skill":
        ui_surface.blit(font.render("Magic:",True,("purple")),(text_w,rect_h))
        pygame.draw.rect(ui_surface,(100,100,100),(rect_w,rect_h+int(25*scale),btn_w,bar_h))
        pygame.draw.rect(ui_surface,("purple"),(rect_w,rect_h+int(25*scale),cast_time*btn_w/100,bar_h))
    screen.fill((0, 0, 0))              # clear real screen
    screen.blit(ui_surface, (0, 0))     # paste UI onto it
    pygame.display.flip()
pygame.quit()
sys.exit()
