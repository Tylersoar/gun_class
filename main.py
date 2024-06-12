import random

class Weapon:
    def __init__(self, name, damage, durability, weight):
        self.name = name
        self.base_damage = damage  
        self.damage = damage
        self.durability = durability
        self.weight = weight

    def attack(self):
        critical_number_a = random.randint(1, 5)
        critical_number_b = random.randint(1, 5)

        if critical_number_a == critical_number_b:
            self.damage = int(self.base_damage * 1.25)
            attack_message = f"{self.name} lands a critical hit and deals {self.damage} damage!"
        else:
            self.damage = self.base_damage
            if self.durability > 0:
                attack_message = f"{self.name} attacks and deals {self.damage} damage!"
                self.durability -= 1
                attack_message += f"\nThe new durability is now {self.durability}"
            else:
                attack_message = f"{self.name} has broken!"

        return attack_message

    def repair(self):
        print("Repairing", self.name, "...")
        self.durability += 2
        print(f"{self.name} has been repaired to {self.durability} durability.")

    def __str__(self):
        return f"{self.name} - Damage: {self.damage}, Durability: {self.durability}, Weight: {self.weight}"

# Example usage:
gun = Weapon("Vector", 5, 900, 3.9)

print(gun)
print(gun.attack())
