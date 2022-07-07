class Dog():
    '''Модель собаки'''
    def __init__(self,name,age):
        '''Инициируем атрибуты класса'''
        self.name = name
        self.age = age
    
    def sit(self):
        print (f'{self.name} is now sitting')
    
    def roll_over(self):
        print (f'{self.name} rolled over!')

my_dog = Dog('willie',6)
print (f"My dog's name is {my_dog.name}.")
print (f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',3)
print (f"\nMy dog's name is {your_dog.name}.")
print (f"My dog is {your_dog.age} years old.")
your_dog.sit()
