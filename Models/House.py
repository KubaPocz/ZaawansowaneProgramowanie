from Models.Property import Property
class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} m², {self.rooms} rooms, Price: {self.price}, Address: {self.address}, Plot: {self.plot} m²"