from Vehicle import Vehicle
class supercar(Vehicle):
    def __init__(self, brand, model, year, engine, doors, horsepower,price):
      super().__init__(brand, model, year)
      self._engine = engine
      self._doors = doors
      self._horsepower = horsepower
      self._price = price

    def display_info(self):
      return f"supercar: {self._brand} {self._model} {self._engine} engine {self._horsepower} horsepower, is {self._price} {self._doors} doors ({self._year})"
    
    def honk(self):
      return "Beep Beep"
my_supercar = supercar(brand = 'Buggati', model='Buggati Chiron', year = '2024', engine='W16', doors='2', horsepower='1,578',price='$4,999,999')
print(my_supercar.display_info())
print(my_supercar.honk())
    