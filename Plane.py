class Plane(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)  # Call the initializer of the parent class
        self.capacity = capacity

    def display_info(self):
        super().display_info()  # Call the parent method to display common info
        print(f"Capacity: {self.capacity} passengers")

    def take_off(self):
        print(f"The {self.model} is now taking off.")

    def land(self):
        print(f"The {self.model} has landed safely.")

if __name__ == "__main__":
    my_plane = Plane("Boeing", "747", 416)
    my_plane.display_info()
    my_plane.start()
    my_plane.take_off()
    my_plane.land()
    my_plane.stop()
