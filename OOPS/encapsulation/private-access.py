# class Factory:
#     __a = 'Pune'

#     def __show(self):
#         print("This is a factory instance method")

# class BhopalFactory(Factory):
#     def show2(self):
#         print(super().__a)


# obj = BhopalFactory()
# obj.show2()


# class Animal:
#     __name = "Lion"

#     def __show(self):
#         print("Animal show")

# animalObj = Animal()
# print(animalObj.__name)

class Animal:
    __name = "Lion"

    def show(self):
        print(f"Animal show : {Animal.__name}") # By using public method obj access private attribute

animalObj = Animal()
animalObj.show()
