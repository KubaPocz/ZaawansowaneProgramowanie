from Models.Property import Property
class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} m², {self.rooms} rooms, Price: {self.price}, Address: {self.address}, Floor: {self.floor}"