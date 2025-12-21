class Inventory:
    def __init__(self, weapon="Empty", health_potion=0, mana_potion=0,gold=200, armor="Empty"):
        self.weapon = weapon
        self.armor = armor
        self.gold=gold
        self.items = {
            "health potion": health_potion,
            "mana potion": mana_potion
        }
        self.accesory=[]

    def add_item(self, item, amount=1):
        stackable=["health potion","mana potion","gold","slime gel","sticky core","fang"]
        weapon=["sword","dagger"]
        # Non-stackable items
        if item in stackable:
            # Stackable items
            if item in self.items:
                self.items[item] += int(amount)
            else:
                self.items[item] = int(amount)
            print(f"{amount} {item}(s) added to inventory")
        else:
            if item in weapon:
                self.weapon = item
            if item.endswith("armor"):
                self.armor = item
            else:
                self.accesory.append(item)
            print(f"{item} equipped!")

    def remove_item(self, item, amount=1):
        if item == "gold" and self.gold>=amount:
            self.gold-=amount
            return True
        elif item in self.items and self.items[item]>=amount:
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
        lines.append(f"        gold:\n            -{self.gold}")
        lines.append(f"        weapon:\n           -{self.weapon}")
        lines.append(f"        armor:\n           -{self.armor}")
        if self.accesory:
            lines.append(f"        accesory:\n")
            for item in self.accesory:
                lines.append(f"          -{item}")
        else:
            lines.append(f"        accesory:\n          -empty")
        if self.items:
            lines.append("        items:")
            for name, count in self.items.items():
                lines.append(f"           -{name}: {count}")
        else:
            lines.append("        items:\n           -Empty")

        return "\n".join(lines)
