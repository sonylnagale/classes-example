class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def display_info(self):
        """Abstract method to display vehicle info."""
        return f"{self._brand} {self._model} ({self._year})"
    
    def honk(self):
        """A general honk sound for all vehicles."""
        return "Beep beep!"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        # Call the parent class constructor
        super().__init__(brand, model, year)
        self._number_of_doors = number_of_doors

    def honk(self):
        return "Honk honk! This is a car!"

    def open_trunk(self):
        return "The trunk is now open."

