# Inter Planetary Weights by James Ross
# Declare Named Constants for planets
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

# Input Name
sName = input('What is your name? ')

# Input Weight
nWeight = input('What is your weight? ')

# Cast Weight variable to float
nWeight = float(nWeight)

# Multiply each planet's surface gravity factor by inputted weight
nMercury = MERCURY * nWeight
nVenus = VENUS * nWeight
nMoon = MOON * nWeight
nMars = MARS * nWeight
nJupiter = JUPITER * nWeight
nSaturn = SATURN * nWeight
nUranus = URANUS * nWeight
nNeptune = NEPTUNE * nWeight
nPluto = PLUTO * nWeight

# Output name then output weight variations per planet using 10 positions and format to 2nd decimal place
print(sName, 'here are your weights on our Solar System\'s Planets:')
print('Weight on Mercury:      ' + format(nMercury, '10.2f'))
print('Weight on Venus:        ' + format(nVenus, '10.2f'))
print('Weight on Moon:         ' + format(nMoon, '10.2f'))
print('Weight on Mars:         ' + format(nMars, '10.2f'))
print('Weight on Jupiter:      ' + format(nJupiter, '10.2f'))
print('Weight on Saturn:       ' + format(nSaturn, '10.2f'))
print('Weight on Uranus:       ' + format(nUranus, '10.2f'))
print('Weight on Neptune:      ' + format(nNeptune, '10.2f'))
print('Weight on Pluto:        ' + format(nPluto, '10.2f'))
