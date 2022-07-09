import car 

my_bmv = car.Car('BMW','model S', 2015)
print (f'\n{my_bmv.get_descriptive_name()}')


my_electric_car = car.ElectricCar('tesla','model S', 2022)
print (f'\n{my_electric_car.get_descriptive_name()}')
my_electric_car.battary.describe_battary()
my_electric_car.battary.get_range()
