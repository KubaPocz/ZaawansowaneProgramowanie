class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} m², {self.rooms} rooms, Price: {self.price}, Address: {self.address}, Plot: {self.plot} m²"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} m², {self.rooms} rooms, Price: {self.price}, Address: {self.address}, Floor: {self.floor}"


house = House(120, 5, 350000, "Kraków, ul. Długa 10", 500)
flat = Flat(60, 3, 200000, "Warszawa, ul. Marszałkowska 25", 2)

print(house)
print(flat)
