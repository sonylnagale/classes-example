from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, miles_driven):
        super().__init__(brand, model, year)
        self.doors = doors
        self.miles_driven=miles_driven

    def display_info(self):
        """Override the parent class method for a Car."""
        return f"Car: {self._brand} {self._model}, {self.doors} doors ({self._year})"

    def honk(self):
        """Specific implementation for a car."""
        return "Honk honk!"
    
    def miles_driven(self):
        return f"{self.miles_driven}" 
