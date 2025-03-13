import os
os.system('clear')

class Spaceship():
    def __init__(self, name, hull_strength, shields, firepower, fuel, alive_status):
        self.name = name
        self.hull_strength = hull_strength
        self.shields = shields
        self.firepower = firepower
        self.fuel = fuel
        self.alive_status = alive_status
        
            
    def attack(self, enemy_ship):
        remaining_damage = 0
        if enemy_ship.shields - self.firepower < 0:
            remaining_damage = self.firepower - enemy_ship.shields
            enemy_ship.shields = 0
        elif enemy_ship.shields != 0:
            enemy_ship.shields -= remaining_damage
        else:
            enemy_ship.hull_strength -= self.firepower
        if remaining_damage != 0:
            enemy_ship.hull_strength -= remaining_damage
            print(f"{self.name} attacks {enemy_ship.name} for {self.firepower} damage.")
        if enemy_ship.hull_strength <= 0:
            enemy_ship.alive_status = "Dead"
            print(f"{self.name} has successfully eliminated {enemy_ship.name} with {self.firepower} damage.")
    
    
        self.shields -= enemy_ship.firepower
        if self.shields <= 0: # If the shields are at 0 or less, move firepower to the hull
            self.hull_strength -= enemy_ship.firepower
        print(f"{self.name} takes {enemy_ship.firepower} damage from {enemy_ship.name}'s laser cannons")
        if self.hull_strength <= 0:
            print(f"{self.name} has been destroyed.")
    
    def status(self):
        print(f" Current status for {self.name} is: Hull: {self.hull_strength}, Shields: {self.shields}, Fuel: {self.fuel}, Status: {self.alive_status}")




my_ship = Spaceship("Thunderbird", 100, 50, 100, 100, "Alive")
enemy_ship = Spaceship("Bomboclat", 150, 75, 25, 500, "Alive")

my_ship.status()
enemy_ship.status()

attack = my_ship.attack(enemy_ship)




# Asks user if they want to attack again or see stats after each attack

choice = int(input("Do you want to attack again (1), do you want to see stats (2), or quit (3)?"))
while True:
    if choice == 1:
        my_ship.attack(enemy_ship)
    elif choice == 2:
        my_ship.status()
        enemy_ship.status()
        choice = int(input("Do you want to attack again (1), or do you want to see stats (2)?"))
    elif choice == 3:
        break


# Creating a fleet

class Fleet():
    def __init__(self):
        self.ships = []
        
    def add_ship(self, ship):
        self.ships.append(ship)
        
    def remove_ship(self, ship):
        self.ships.remove(ship)
        
    def status(self):
        for ship in self.ships:
            ship.status()
            
    def attack(self, enemy_fleet):
        for ship in self.ships:
            for enemy_ship in enemy_fleet.ships:
                ship.attack(enemy_ship)
                if enemy_ship.alive_status == "Dead":
                    enemy_fleet.remove_ship(enemy_ship)
                    print(f"{enemy_ship.name} has been removed from the fleet.")
                if ship.alive_status == "Dead":
                    self.remove_ship(ship)
                    print(f"{ship.name} has been removed from the fleet.")

my_fleet = Fleet()

my_fleet.add_ship(my_ship)

print(my_fleet.status)