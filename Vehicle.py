class Vehicle:
    def __init__(self, brand, model, year, weight):
        self._brand = brand
        self._model = model
        self._year = year
        self.weight = weight

    def display_info(self):
        """Abstract method to display vehicle info."""
        return f"{self._brand} {self._model} ({self._year}) ({self.weight})"
    
    def honk(self):
        """A general honk sound for all vehicles."""
        return "Beep beep!"


#Change any of the change classes and add a child class. -Jeremiah

    
class Boat(Vehicle):
    def __init__(self, brand, model, year, weight, boat_type):
        # Call the parent class constructor
        super().__init__(brand, model, year, weight)
        self.boat_type = boat_type  # Initialize the boat_type attribute

    def display_info(self):
        return f"{super().display_info()}, Type: {self.boat_type}"

    def honk(self):

        return "Pew, pew, rawrrrr!"
# Create an instance of the Boat class
yacht = Boat(brand="Sunseeker", model="Predator", year=2023, weight="12000kg", boat_type="Yacht")

# Call methods and print output
print(yacht.display_info()) 
print(yacht.honk())