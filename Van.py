from Vehicle import Vehicle

class Van(Car):
    def __init__(self, brand, model, year, doors, cargo_space):
        super().__init__(brand, model, year, doors)
        self.cargo_space = cargo_space  # in cubic feet

    def display_info(self):
        """Override the Car class method for a Van."""
        return (
            f"Van: {self._brand} {self._model}, {self.doors} doors "
            f"({self._year}), Cargo Space: {self.cargo_space} cubic feet"
        )

    def load_cargo(self, weight):
        """Loading cargo into the van."""
        return f"Loading {weight} lbs of cargo into the {self._brand} {self._model}."
