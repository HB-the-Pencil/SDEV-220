from pygments.lexers import make


class Vehicle:
    """Represent a vehicle of some kind."""
    def __init__(self, kind: str):
        self.kind = kind

    def __str__(self):
        return self.kind

    def __repr__(self):
        return f"Vehicle('{self.kind}')"


class Car(Vehicle):
    """Represent a car."""
    def __init__(
            self,
            year: int,
            make: str,
            model: str,
            doors: int,
            sunroof: bool):
        """
        Initialize a car.

        :param year: Year the car was made.
        :param make: Make of the car.
        :param model: Model of the car.
        :param doors: Number of doors (2 or 4).
        :param sunroof: Whether the car has a sunroof.
        """
        super().__init__('Car')

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.sunroof = sunroof

    def __str__(self):
        """
        Return a string representation of the car.

        :return: Returns a string describing the car.
        """
        info = (f"Model: {self.year} {self.make} {self.model}\n"
        f"{self.doors}-door car {'with' if self.sunroof else 'without'} "
        f"sunroof")
        return info

    def __repr__(self):
        """
        Produce the function call used to create the car.

        :return: Returns a string that could be used to create the same car.
        """
        string = (f"Car({self.year}, '{self.make}', '{self.model}', "
                  f"{self.doors}, {self.sunroof})")
        return string


def create_car():
    """
    Ask the user to create a car.

    :return: Returns an instance of the Car class.
    """
    info = input(
        "Please input your model of car in the format 'year make model'.\n"
        "Ex: 2006 Honda Accord\n"
        "> "
    )
    try:
        year, make, *model = info.split(" ")
    except ValueError:
        print("Fatal error: Not enough information. Please try again.")
        return

    try:
        year = int(year)
    except ValueError:
        print("Fatal error: Year must be a number. Please try again.")
        return

    if type(model) is list:
        model = " ".join(model)

    doors = input("\nPlease input the number of doors (2 or 4).\n> ")
    try:
        doors = int(doors)
        if doors not in [2, 4]:
            raise IndexError
        if doors < 0:
            raise ValueError
    except ValueError:
        print("Fatal error: Doors must be a number greater than 0."
              "Please try again.")
        return
    except IndexError:
        print("Warning: Doors should be either 2 or 4.")

    sunroof = input("Does your car have a sunroof? (y/n)\n> ")

    if sunroof.lower().strip() == 'y':
        sunroof = True
    else:
        sunroof = False

    return Car(year, make, model, doors, sunroof)


car = create_car()

print(car)
print()
print(repr(car))
