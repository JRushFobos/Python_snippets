class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name= f'{self.make} {self.model} {self.year}'
        return long_name.title()

    #Прямое изменение атрибута
    def read_odometr(self):
        print (f'This car has {self.odometr_reading} mile on it.')
    
    '''Изменениет атрибута с использованием метода''' 
    def update_odometr(self,mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print ("You can't roll back an odometer!")

    '''Изменение атрибута с приращиванием'''
    def increment_odometer(self,miles):
        self.odometr_reading += miles

class ElectricCar(Car):
    '''Автомобиль со спецификой электромобиля.'''
    def __init__(self,make,model,year):
        '''Инициализация атрибутов класса'''
        super().__init__(make,model,year)
        '''Инициируем атрибуты класса-потомка'''
        self.battary_size = 75
    
    '''Методы класса потомка'''
    def describe_battary(self):
        print (f'This car has a{self.battary_size} KWh battary.')

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battary()