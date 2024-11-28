from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def display_info(self):
        """Override the parent class method for a Truck."""
        return f"Truck: {self._brand} {self._model}, Max load: {self.max_load} tons ({self._year})"

    def honk(self):
        """Specific implementation for a truck."""
        return "HOOOOONK!"
my_truck = Truck(brand = 'Peterbilt', model = 'Model 379', year = '2007', max_load= '54,000lbs')
print(my_truck.display_info())
print(my_truck.honk())