from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, arrival):
        super().__init__(brand, model, year)
        self.arrival = arrival

    def display_info(self):
        return f"Bus: {self._brand} {self._model}, Max load: {self.max_load} tons({self._year})"

    def honk(self):
        return "Honk honk!"

    def display_Arrival(self):
        return "Arrival time."