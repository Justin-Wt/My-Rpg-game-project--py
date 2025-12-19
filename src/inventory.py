class Inventory:
    def __init__(self, weapon="Empty", health_potion=0, mana_potion=0, armor="Empty"):
        self.weapon = weapon
        self.armor = armor
        self.items = {
            "health potion": health_potion,
            "mana potion": mana_potion
        }

    def add_item(self, item, amount=1):
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def remove_item(self, item, amount=1):
        if item in self.items and self.items[item]>=amount:
            self.items[item] -= amount
            if self.items[item] == 0:
                del self.items[item]
            print(f"you've used {amount} {item}")
            return True
        else:
        	print(f"you didnt have enough {item}")
        	return False
    def has_item(self, item):
        return item in self.items

    def __str__(self):
        lines = []
        lines.append(f"        weapon:\n           -{self.weapon}")
        lines.append(f"        armor:\n           -{self.armor}")

        if self.items:
            lines.append("        items:")
            for name, count in self.items.items():
                lines.append(f"           -{name}: {count}")
        else:
            lines.append("        items:\n           -Empty")

        return "\n".join(lines)