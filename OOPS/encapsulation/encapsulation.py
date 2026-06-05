# class Factory:
#     a = 'Pune'

#     def show(self):
#         print("This is a factory instance method")

# class BhopalFactory(Factory):
#     def show2(self):
#         print(super().a)


# obj = BhopalFactory()
# obj.show2()

# protected access modifier is not working in python, still access a in bhopal factory

class Factory:
    _a = 'Pune'

    def _show(self):
        print("This is a factory instance method")

class BhopalFactory(Factory):
    def show2(self):
        print(super()._a)


obj = BhopalFactory()
obj.show2()