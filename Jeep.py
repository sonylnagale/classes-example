from Vehicle import Vehicle

class Jeep(Vehicle):
    def __init__(self, brand, model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels

    def display_info(self):
        
        return f"Jeep: {self._brand} {self._model}, Wheels: {self.wheels}, ({self._year})"

    def honk(self):
        
        return "BRRRRRR!"