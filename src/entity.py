class Entity:
    def __init__(self, name, hp, defense, strength):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.strength = strength
        self.statuses = []
    def has_status(self, name):
        return any(status.name == name for status in self.statuses)
    def can_act(self):
        return not self.has_status("stun")
    def apply_status(self, status):
        status.on_apply(self)
        self.statuses.append(status)

    def update_statuses(self):
        for status in self.statuses[:]:
            status.on_tick(self)
            if status.is_expired():
                status.on_end(self)
                self.statuses.remove(status)
