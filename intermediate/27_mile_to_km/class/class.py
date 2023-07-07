def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 4, 5, 6))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


# print(calculate(5, add=3, multiply=5))


class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan",)
print(my_car.model)
