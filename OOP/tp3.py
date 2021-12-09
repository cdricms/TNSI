
class Vehicle():
    index: int = 0
    name: str = ""
    max_speed: int = 1
    acceleration: int = 0

    position: int = 0
    speed: int = 0

    def __init__(self, index: int, name: str, max_speed: int, acceleration: int):
        self.index = index
        self.name = name
        self.max_speed = max_speed
        self.acceleration = acceleration

    def move_forward(self, duration: int):
        while self.speed < self.max_speed:
            self.speed += self.acceleration
            self.position += self.speed


# intanciation des objets
vehicle_list = []
vehicle_list.append(Vehicle(0, "Millennium Falcon", 300, 26))
vehicle_list.append(Vehicle(1, "Formule 1", 90, 49.05))

# algorithme principal
while True:
    print("----- LISTE DES VÉHICULES ------")
    for vehicle in vehicle_list:
        print(vehicle.index, vehicle.name, "/ vitesse max :", vehicle.max_speed, "m/s / accélération :",
              vehicle.acceleration, "m/s²")
    print("---------------------------")
    print("Quel véhicule souhaitez-vous tester?")
    vehicule_index = int(input())
    print("Combien de secondes souhaitez-vous le faire avancer (nombre entier)?")
    duration = int(input())
    distance = round(vehicle_list[vehicule_index].move_forward(duration), 2)
    print(vehicle_list[vehicule_index].name, "a parcouru",
          distance, "m, en ", duration, "s.")
    vehicle_list[vehicule_index].position = 0
    print("---------------------------")
