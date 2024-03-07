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
        self.dodge_uses = 2

    def attack(self, enemy):
        damage = random.randint(10, 20)
        ammo_consumed = random.randint(3, 8)
        self.ammo -= ammo_consumed
        enemy.health -= damage
        print(f"{self.name} attacks with {self.weapon}! {enemy.name} takes {damage} damage.")
        print(f"Ammo consumed: {ammo_consumed}")

    def use_heal(self):
        print(f"{self.name} stands by. A healing wave fills your soul.")
        heal_amount = int(0.35 * self.max_health)
        if self.health + heal_amount <= self.max_health:
            self.health += heal_amount
            print(f"{self.name} heals for {heal_amount} health.")
        else:
            heal_amount = self.max_health - self.health
            self.health = self.max_health
            print(f"{self.name} heals for {heal_amount} health.")

    def melee(self, enemy):
        damage = random.randint(5, 15)
        enemy.health -= damage
        print(f"{self.name} strikes {enemy.name}! {enemy.name} takes {damage} damage.")

    def dodge(self):
        if self.dodge_uses > 0:
            print(f"{self.name} dodges the enemy's attack!")
            self.dodge_uses -= 1
        else:
            print("You have no more dodge uses left!")

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(5, 15)
        if random.random() > 0.7:  # 70% chance to hit
            player.health -= damage
            print(f"{self.name} attacks! {player.name} takes {damage} damage.")
        else:
            print(f"{self.name} attacks! But {player.name} dodges the attack!")

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
    print("???: Take this Auto Rilfe.")
    time.sleep(1)
    print("Faint-Light Auto Rifle added to your inventory.")
    time.sleep(2)
    print("???: We need to leave. Do you at least remember your name?")
    time.sleep(2)

    name = input("What's your name?: ")
    player = Guardian(name)
    enemy_types = ["Fallen Captain", "Fallen Vandal", "Fallen Dreg", "Fallen Shank"]
    enemy = Enemy(random.choice(enemy_types), 50)

    print(f"???: You don't strike me as a {player.name}, but sure.")
    time.sleep(3)
    print()
    print('Fallen:"Klix\'ix, skra\'an ven Guardian!"')

    print(f"???: 'Get ready, {player.name}! A {enemy.name} approaches.'")

    enemy_turn_count = 0

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}: Health - {player.health}, Ammo - {player.ammo}")
        print(f"{enemy.name}: Health - {enemy.health}")

        action = input("\nChoose an action: (1) Attack, (2) Heal, (3) Melee, (4) Dodge, (5) Flee: ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.use_heal()
        elif action == "3":
            player.melee(enemy)
        elif action == "4":
            player.dodge()
        elif action == "5":
            print("You flee from battle!")
            break
        else:
            print("Invalid action. Try again.")

        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy.name}!")
            break

        enemy.attack(player)
        if player.health <= 0:
            print("Your Light is Consumed...")
            break

        enemy_turn_count += 1
        if enemy_turn_count % 3 == 0:
            player.dodge_uses = 2

if __name__ == "__main__":
    main()
