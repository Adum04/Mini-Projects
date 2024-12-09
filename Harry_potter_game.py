import random


class DarkLord:
    def __init__(self):
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"The Dark Lord's health is now {self.health}.")

    def is_defeated(self):
        return self.health == 0


class Wizard:
    def __init__(self, name):
        self.name = name
        self.spells = {
            "Expelliarmus": 15,
            "Reducto": 25,
            "Stupefy": 30,
            "Patronus": 40,
            "Avada Kedavra": 100,
        }

    def cast_spell(self, spell_name, dark_lord):
        if spell_name in self.spells:
            damage = self.spells[spell_name]
            print(f"{self.name} casts {spell_name} and deals {damage} damage!")
            dark_lord.take_damage(damage)
        else:
            print(f"{spell_name} is not a recognized spell!")


# Simulating the battle
name = input("Choose your Wizard: ")
dark_lord = DarkLord()
wizard = Wizard(name)

print("The Dark Lord has appeared! Prepare for battle!")

# Battle loop
while not dark_lord.is_defeated():
    spell = input(
        "Choose a spell to cast (Expelliarmus, Reducto, Stupefy, Patronus, Avada Kedavra): "
    ).strip()
    wizard.cast_spell(spell, dark_lord)
    if dark_lord.is_defeated():
        print("The Dark Lord has been defeated! Victory!")
        print(f"The 'Elder Wand' now Belongs to {name} !")
        break
    else:
        # The Dark Lord attacks back randomly
        damage = random.randint(5, 20)
        print(f"The Dark Lord strikes back and deals {damage} damage!")
