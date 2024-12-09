from Vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type

    def display_info(self):
        """Override the parent class method for a Boat."""
        return f"Boat: {self._brand} {self._model}, Type: {self.boat_type} ({self._year})"

    def honk(self):
        return "Honk!"

    def anchor(self):
        return "Anchoring the boat."