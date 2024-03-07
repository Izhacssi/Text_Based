import time
import sys
import random


class Guardian:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.weapon = "Faint-Light Auto Rifle"
        self.ammo = 100
        self.inventory = []
        self.dodge_uses = 3
        self.heal_uses = 3
        self.turn_count = 0

    def attack(self, enemy):
        damage = random.randint(10, 20)
        ammo_consumed = random.randint(3, 8)
        self.ammo -= ammo_consumed
        enemy.health -= damage
        print(
            f"{self.name} attacks with {self.weapon}! {enemy.name} takes {damage} damage.")
        print(f"Ammo consumed: {ammo_consumed}")

    def use_heal(self):
        print(f"{self.name} stands by. A healing wave fills your soul.")
        heal_amount = random.randint(
            int(0.23 * self.max_health), int(0.35 * self.max_health))
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health.")
        self.heal_uses -= 1

    def melee(self, enemy):
        damage = random.randint(5, 15)
        enemy.health -= damage
        print(f"{self.name} strikes {enemy.name}! {enemy.name} takes {damage} damage.")

    def dodge(self):
        if self.dodge_uses > 0:
            print(f"{self.name} attempts to dodge the enemy's attack!")
            dodge_chance = random.randint(1, 100)
            if dodge_chance > 30:
                print(f"{self.name} successfully dodges the enemy's attack!")
            else:
                print(f"{self.name} fails to dodge the enemy's attack!")
                damage = random.randint(5, 15)
                self.health -= damage
                print(f"{self.name} takes {damage} damage!")
            self.dodge_uses -= 1
        else:
            print("You have no more dodge attempts left.")


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(5, 15)
        player.health -= damage
        print(f"{self.name} attacks! {player.name} takes {damage} damage.")


def main():
    print("Destiny - Act 1: Awakening")
    time.sleep(3)
    print("You wake up in the middle of a field.")
    time.sleep(3)
    print("You have no idea where you are, how you got here, or how long you've been here.")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("\"AAAAAAAGHHHHHHHHHH!\"")
    time.sleep(3)
    print("A howl. Sharp. Like that of a monster.")
    time.sleep(3)

    print("???: I know you don't know who I am, but I'll explain later.")
    print("You're a Guardian. Forged in Light.")
    time.sleep(3)
    print("???: Take this Faint-Light Auto Rilfe.")
    time.sleep(1)
    print("Faint-Light Auto Rifle added to your inventory.")
    time.sleep(2)
    print("???: We need to leave. Do you at least remember your name?")
    time.sleep(2)

    name = input("What's your name?: ")
    player = Guardian(name)
    enemy_types = ["Fallen Captain", "Fallen Vandal",
                   "Fallen Dreg", "Fallen Shank"]
    enemy = Enemy(random.choice(enemy_types), random.randint(50, 100))

    print(f"???: You don't strike me as a {player.name}, but sure.")
    time.sleep(3)
    print()
    print('Fallen:"Klix\'ix, skra\'an ven Guardian!"')

    print(f"???: 'Get ready, {player.name}! A {enemy.name} approaches.'")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}: Health - {player.health}, Ammo - {player.ammo}")
        print(f"{enemy.name}: Health - {enemy.health}")

        action = input(
            "\nChoose an action: (1) Attack, (2) Heal, (3) Melee, (4) Dodge, (5) Flee: ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.use_heal()
        elif action == "3":
            player.melee(enemy)
        elif action == "4":
            player.dodge()
        elif action == "5":
            flee_chance = random.randint(1, 100)
            if flee_chance <= 55:  # 55% chance to flee
                print("You successfully flee from battle!")
                break
            else:
                print("You failed to flee and must continue the battle!")
        else:
            print("Invalid action. Try again.")

        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy.name}!")
            break

        enemy.attack(player)
        if player.health <= 0:
            print("Your Light is Consumed...")
            break


if __name__ == "__main__":
    main()

# Boogers
# FeatureBoogers

# Sup Chawchoe
