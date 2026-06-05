def decorate(funct):

    def wrapper(*args, **kwargs):
        print("This is before the function call.")
        funct(*args, **kwargs)
        print("This is after the function call.")
    return wrapper

@decorate
def addition(a,b):
    print("Addition is : ", a + b )


addition(10,20)