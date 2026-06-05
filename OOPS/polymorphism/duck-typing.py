class Animal:
    def show(self):
        print("This is animal show.")
    
class Human:
    def show(self):
        print("This is human show.")


obj = Animal()
obj1 = Human();

# Duck-Typing - if user only able to see below obj access to same show method

obj.show()
obj1.show()
