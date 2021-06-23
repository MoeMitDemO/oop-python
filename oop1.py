from Classes.Dog import Dog

d = Dog()
d.setName(input('Name des Hundes? '))
d.setColor(input('Farbe des Hundes? '))

print('Name: \t' + d.getName() + '\nFarbe: \t' + d.getColor())