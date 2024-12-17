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
    
class Plane(Vehicle):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self._engine_type = engine_type

    def display_info(self):
        base_info = super().display_info()  
        return f"{base_info} - {self._engine_type} engine"

    def honk(self):
        return "Whoooosh!"

#Testing the code
my_plane = Plane("Boeing", "747", 2019, "Jet")
print(my_plane.display_info())  
print(my_plane.honk())          

    def brake(self):
        print("Braking the car.")

