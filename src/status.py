class StatusEffect:
    def __init__(self, name, damage=0, duration=3):
        self.name = name
        self.damage = damage
        self.duration = duration

    def on_apply(self, target):
        if self.name=="Stun":
            target.stunned=True
        print(f"{target.name} is affected by {self.name}!")

    def on_tick(self, target):
        if self.damage > 0:
            target.hp = max(0, target.hp - self.damage)
            print(f"{target.name} takes {self.damage} damage from {self.name}.")

        self.duration -= 1

    def is_expired(self):
        return self.duration <= 0

    def on_end(self, target):
        if self.name=="Stun":
            target.stunned=False
        print(f"{self.name} on {target.name} has ended.")
    
def create_status(name):
    library = {
        "poison": StatusEffect("Poison", damage=2, duration=3),
        "bleed": StatusEffect("Bleed", damage=3, duration=2),
        "stun": StatusEffect("Stun", damage=0, duration=1),
    }
    return library.get(name)
