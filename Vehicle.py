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


class Bike(Vehicle):
    def __init__(self, brand, model, year, has_gears):
        super().__init__(brand, model, year)
        self.has_gears = has_gears

    def display_info(self):
        """Overide display_info to include specific bike info."""
        return f"{super().display.info()} - {'with gears' if self.has_gears else 'without the gears'}"

    def ring_bell(self):
        """Specific method for bikes."""
        return "Ring ring!""
