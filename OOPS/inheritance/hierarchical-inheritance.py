class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(Factory):
    def __init__(self, material, zips, brand):
        super().__init__(material, zips)
        self.brand = brand

class MumbaiFactory(Factory):
    def __init__(self, material, zips, location):
        super().__init__(material, zips)
        self.location = location

obj1 = BhopalFactory("Leather", 3, 'maroon')
print(f"Bhopal: {obj1.material}, {obj1.zips}, {obj1.color}")

obj2 = PuneFactory("Cotton", 5, 'XYZ Brand')
print(f"Pune: {obj2.material}, {obj2.zips}, {obj2.brand}")

obj3 = MumbaiFactory("Silk", 2, 'Central Mumbai')
print(f"Mumbai: {obj3.material}, {obj3.zips}, {obj3.location}")
