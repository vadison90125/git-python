class Car:
    Model = None
    Color = None
    Age = None

    def __init__(self, Model, Color, Age):
        self.Model = Model
        self.Color = Color
        self.Age = Age
        self.vivod_info()

    def vivod_info(self):
        print('Model:', self.Model, '\n', 'Cvet:', self.Color, '\n', 'God:   ', self.Age)


class Bus(Car):
    Wheels = 18
    def __init__(self, Wheels, Model, Color, Age):
        self.Model = Model
        self.Color = Color
        self.Age = Age
        self.Wheels = Wheels

    def vivod_info(self):
        print('Model:', self.Model, '\n', 'Cvet:', self.Color, '\n', 'God:   ', self.Age)
        print('Колёса:', self.Wheels)


# Car1 = Car('Ferrari', 'red', 3)

Bus1 = Bus(20, 'MAN', 'red', 3)
Bus1.vivod_info()

#Car1.vivod_info()



