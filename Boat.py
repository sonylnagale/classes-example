from Vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, model, year, length, boat_type):
        super().__init__(brand, model, year)
        self.length = length
        self.boat_type = boat_type

    def display_info(self):
        """Override the parent class method to include boat-specific details."""
        return f"Boat: {self._brand} {self._model}, {self.length} ft ({self._year}), Type: {self.boat_type}"

    def honk(self):
        """Specific implementation for a boat horn."""
        return "Boat horn: TOOT TOOT!"

    def is_sailboat(self):
        """Check if the boat is a sailboat."""
        return self.boat_type.lower() == "sailboat"

    def boat_summary(self):
        """Provides a detailed summary of the boat."""
        return f"{self.boat_type.capitalize()} - {self._brand} {self._model}, built in {self._year}, {self.length} ft long."
