class StatusEffect:
    def __init__(self,name,damage=0,duration=3):
        self.name=name
        self.damage=damage
        self.duration=duration
    def on_apply(self,target):
        pass
    def on_start(self,target):
        pass
    def on_end(self,target):
        target.hp-=self.damage
        print(f"The {self.name} has damage {target.name} for {self.damage}")
        self.duration-=1