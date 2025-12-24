from status import  StatusEffect
class Entity:
    def __init__(self,name,hp,defense,strength):
        self.name=name
        self.hp=hp
        self.defense=defense
        self.strength=strength
        self.statuses=[]
    def apply_status(self,status):
        self.statuses.append(status)
        status.on_apply(self)
    def status_attack(self):
        for status in self.statuses[:]:
            status.on_start(self)
            status.on_end(self)
            if status.duration<=0:
                self.statuses.remove(status)
                print(f"the {status} on {self.name} has worn off")
    def is_immune(self,status):
        return False
    