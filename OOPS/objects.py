class Factory:
    a = 11 # attribute

    def hello(self): # method
        print("How are you")

    print("Hello, I am getting initialized.")

# Factory()

# print(Factory().a) # Attribute print

# Factory().hello() # Method invoked

obj = Factory()

print(obj.a)
obj.hello()


