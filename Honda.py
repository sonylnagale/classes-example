from Vehicle import Vehicle

class Honda(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self._number_of_doors = number_of_doors

    def display_info(self):
        """Override the parent class method for a Car."""
        return f"Car: {self._brand} {self._model}, {self.doors} doors ({self._year})"    

    def honk(self):
        return "Honk honk! Move!"

    def open_trunk(self):
        return "The trunk is now open."
    
    def fuel(self):
        return "Fuel is full!"
