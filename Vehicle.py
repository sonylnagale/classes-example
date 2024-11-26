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
    
    def brake(self):
        print("Braking the vehicle.")


class Bus(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity

    def display_info(self):
        """Override display_info to include seating capacity."""
        return f"{super().display_info()} with seating capacity of {self.seating_capacity} passengers"

    def capacity_info(self):
        """Specific method for buses."""
        return f"The bus can seat up to {self.seating_capacity} passengers."