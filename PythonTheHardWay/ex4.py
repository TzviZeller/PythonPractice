cars = 100
space_in_a_car = 4.0
drivers = 30
pasangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = pasangers / cars_driven

print('There are', cars, 'cars avaliable')
print('There are only ', drivers, 'drivers avalible')
print('There will be', cars_driven, 'empty cars today')
print('We can trasport', carpool_capacity, 'people today')
print('We have', pasangers, 'to carpool today')
print('We need to put about', average_passangers_per_car, 'in each car')

