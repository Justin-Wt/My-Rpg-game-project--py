class Inventory:
    def __init__(
        self,
        weapon=[],
        armor=[],
        gold=200,
        items={},
        accessories=[]
        ):
        self.weapon = weapon if weapon is not None else[]
        self.armor = armor if armor is not None else[]
        self.gold=gold
        self.items = items if items is not None else {}
        self.accessories=accessories if accessories is not None else []
        
    def add_item(self, item, amount=1):
        stackable=["health potion","mana potion","gold","slime gel","sticky core","fang"]
        weapon=["sword","dagger"]
        # Non-stackable items
        if item in stackable:
            # Stackable items
            if item == "gold":
                self.gold+=amount
            elif item in self.items:
                self.items[item] += int(amount)
            else:
                self.items[item] = int(amount)
            print(f"{amount} {item}(s) added to inventory")
        else:
            if item in weapon:
                self.weapon.append(item)
            if item.endswith("armor"):
                self.armor.append(item)
            else:
                self.accessories.append(item)
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
        lines.append(f"        gold:\n           -{self.gold}")
        lines.append(f"        weapon:")
        for weapons in self.weapon:
            lines.append(f"           -{weapons}")
        else:
            lines.append("           -Empty")
        lines.append(f"        armor:")
        for armors in self.armor:
            lines.append(f"           -{armors}")
        else:
            lines.append("           -Empty")
        if self.accessories is not None:
            lines.append("        accesory:")
            for item in self.accessories:
                lines.append(f"           -{item}")
        else:
            lines.append("        accesory:\n          -Empty")
        if self.items:
            lines.append("        items:")
            for name, count in self.items.items():
                lines.append(f"           -{name}: {count}")
        else:
            lines.append("        items:\n           -Empty")

        return "\n".join(lines)
        
if __name__=="__main__":
    print(inventory)
