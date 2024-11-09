import os
os.system('clear')

class Spaceship():
    def __init__(self, name, hull_strength, shields, firepower, fuel):
        self.name = name
        self.hull_strength = hull_strength
        self.shields = shields
        self.firepower = firepower
        self.fuel = fuel    
    def take_damage(self, damage):
        self.shields -= damage
        if self.shields < 0:
            print(f"{self.name}'s shields have been depleted, hull strength is now at {self.hull_strength}.")
            
    def attack(self, enemy_ship):
        remaining_damage = 0
        if enemy_ship.shields - self.firepower < 0:
            remaining_damage = self.firepower - enemy_ship.shields
            enemy_ship.hull_strength -= remaining_damage
        print(f"{self.name} attacks {enemy_ship.name} for {self.firepower} damage.")
    
    
        self.shields -= enemy_ship.firepower
        if self.shields <= 0: # If the shields are at 0 or less, move firepower to the hull
            self.hull_strength -= enemy_ship.firepower
        print(f"{self.name} takes {enemy_ship.firepower} damage from {enemy_ship.name}'s laser cannons")
        if self.hull_strength <= 0:
            print(f"{self.name} has been destroyed.")
    
    def status(self):
        print(f" Current status for {self.name} is: Hull: {self.hull_strength}, Shields: {self.shields}, Fuel: {self.fuel}")




my_ship = Spaceship("Thunderbird", 100, 50, 100, 1000)
enemy_ship = Spaceship("Bomboclat", 150, 75, 25, 500)

my_ship.status()
enemy_ship.status()

attack = my_ship.attack(enemy_ship)

my_ship.status()
enemy_ship.status()