class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
      
    def display_info(self):
        """Abstract method to display vehicle info."""
        return f"{self._brand} {self._model} ({self._year})"
    
    def honk(self):
        return "Honk Honk!"
    
    def fuel_up(self):
        return "Full tank"
    
    def brake(self):
        print("Braking the car.")
    
