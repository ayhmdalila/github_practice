import random

class Creature():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage")

    def attack(self, opponent):
        opponent.take_damage(self.attack_power)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"
    

class Knight(Creature):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def take_damage(self, damage):
        damage = max(damage - self.armor, 0)
        self.health -= damage
        print(f"{self.name} took {damage} damage after armor reduction!")


class Archer(Creature):
    def __init__(self, name, health, attack_power, crit_chance):
        super().__init__(name, health, attack_power)
        self.crit_chance = crit_chance

    def attack(self, opponent):
        if random.random() <= self.crit_chance:
            damage = self.attack_power * 2
            print(f"{self.name} lands a critical hit!")
        else:
            damage = self.attack_power
        opponent.take_damage(damage)

class SuperKnight(Knight):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power, armor)
        self.super_charge = 0
    
    def increment_charge(self):
        self.super_charge = self.super_charge + 1

    def _use_super(self):
        self.health = self.health + 400
        print(f"{self.name} healed for 400 HP!")
    
    def take_action(self, opponent):
        if self.super_charge >= 10:
            self._use_super()
            self.super_charge = 0
        else:
            self.attack(opponent)

class SuperArcher(Archer):
    def __init__(self, name, health, attack_power, crit_chance):
        super().__init__(name, health, attack_power, crit_chance)
        self.super_charge = 0

    def increment_charge(self):
        self.super_charge = self.super_charge + 1

    def _use_super(self, opponent):
        print(f"{self.name} used his super ability!")
        for _ in range(5):
            self.attack(opponent)

    def take_action(self, opponent):
        if self.super_charge >= 10:
            self._use_super(opponent)
            self.super_charge = 0
        else:
            self.attack(opponent)


import time

def battle(creature1, creature2):
    print("Battle begins!\n============")
    round_num = 1

    while creature1.is_alive() and creature2.is_alive():
        print("============")
        creature1.increment_charge()
        creature2.increment_charge()

        coin = random.choice(["Heads", "Tails"])
        if coin == "Heads":
            creature1.take_action(creature2)
        else:
            creature2.take_action(creature1)

        print("\n")
        print(creature1)
        print(creature2)

        round_num = round_num+1

        time.sleep(2)
    
    if creature1.is_alive():
        print(f"{creature1.name} wins!")
    else:
        print(f"{creature2.name} wins!")

hero = SuperKnight("SuperKnight", 3500, 150, 50)
villain = SuperArcher("SuperArcher", 2000, 250, 0.1)

battle(hero, villain)
