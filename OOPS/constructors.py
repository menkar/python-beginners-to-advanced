class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your objects details are {self.material}, {self.zips}, {self.pockets}")

reebok = Factory("Leather", 3, 2)

campus = Factory("Nylon", 3, 4)

print(reebok.pockets)
print(campus.pockets)

reebok.show()
campus.show()