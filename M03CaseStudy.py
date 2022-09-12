class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        

    def list_information(self):
        print(f"Vehicle Type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of Doors: {self.doors}\nType of Roof: {self.roof} roof.")

not_available = ["truck", "plane", "boat", "broomstick"]
type = input("Is the vehicle a car, truck, plane, boat, or broomstick? ")
while type.lower() != "car":
    if type in not_available:
        print(f"Sorry, {type}s are not available right now.")
    else:
        print(f"Invalid vehicle type [{type}], please try again.")
    type = input("Is the vehicle a car, truck, plane, boat, or broomstick? ")

year = input("What year is the vehicle? ")
year_valid = False
while not year_valid:
    if year.isalpha():
        print(f"Input is not a year [{year}], please try again.]")
        year = input("What year is the vehicle? ")
        continue
    else:
        year_num = int(year)
    if year_num < 1900 or year_num > 2022:
        print(f"Invalid year for vehicle [{year}], please try again.]")
        year = input("What year is the vehicle? ")
        continue
    year_valid = True

make = input("What make is the vehicle? ")
model = input("What model is the vehicle? ")

doors = input("How many doors does the vehicle have? (2 or 4) ")
doors_valid = False
while not doors_valid:
    if doors.isalpha():
        print(f"Input is not a number [{doors}], please try again.]")
        doors = input("How many doors does the vehicle have? (2 or 4) ")
        continue
    else:
        door_num = int(doors)
    if door_num not in [2, 4]:
        print(f"Invalid door number for vehicle [{doors}], please try again.]")
        doors = input("How many doors does the vehicle have? (2 or 4) ")
        continue
    doors_valid = True

roof = input("What type of roof does the vehicle have? (solid, sun) ")
while roof.lower() not in ["solid", "sun"]:
    print(f"Invalid roof type for vehicle [{roof}], please try again.]")
    roof = input("What type of roof does the vehicle have? (solid, sun) ")

picked_automobile = Automobile(type, year, make, model, doors, roof,)
picked_automobile.list_information()