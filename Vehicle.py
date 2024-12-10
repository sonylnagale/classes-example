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
    
    def fuel_up(self):
        return "Full tank"

    def windshield_fluid(self):
        return "Windshield fluid empty."
    
    def brake(self):
        print("Braking the car.")
     
    def fuel(self):
        return "get more fuel when you can"

    def headlight(self):
        return "turn headlight on"
