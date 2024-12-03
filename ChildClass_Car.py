class ChildClass_Car(Car):
    def __init__(self, brand, model, year, doors, battery_capacity):
        super().__init__(brand, model, year, doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        """Override the parent class method for an ChildClass_Car."""
        return (
            f"ChildClass_Car: {self._brand} {self._model}, {self.doors} doors, "
            f"Battery Capacity: {self.battery_capacity} kWh ({self._year})"
        )

    def charge(self):
        """Specific method for charging an electric car."""
        return "Charging the battery..."