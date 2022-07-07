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

new_car = Car('audi','a4','2019')
print (f'\n{new_car.get_descriptive_name()}')

#Прямое изменение атрибута
new_car.odometr_reading = 20
new_car.read_odometr()

'''Изменениет атрибута с использованием метода''' 
print (f'\n{new_car.get_descriptive_name()}')
new_car.update_odometr(50)
new_car.read_odometr()

'''Изменение атрибута с приращиванием'''
my_used_car = Car ('subaru','outback','2015')
print (my_used_car.get_descriptive_name())

my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increment_odometer(100)
my_used_car.read_odometr()