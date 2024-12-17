from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self._seats = seats 

    def display_info(self):
        """Override method to display bus info with seat count."""
        return f"{self._brand} {self._model} ({self._year}) - Seats: {self._seats}"

    def honk(self):
        """Override honk method with a louder sound for the bus."""
        return "HONK HOOONK!"
    
    def load_passengers(self, num_passengers):
        """Simulate loading passengers into the bus."""
        if num_passengers <= self._seats:
            return f"{num_passengers} passengers loaded."
        else:
            return f"Capacity reached!"
