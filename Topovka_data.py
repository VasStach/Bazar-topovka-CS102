from ClassAuto import Auto
from random import choice, randint
topovka_car_list = []
brand_model_dict = {"Škoda":["Fabia", "Octavia", "Superb", "Kodiaq"], "BMW":["315i", "335d", "345M", "525D", "540i", "545M"], "Ford":["Mustang", "F150", "Mondeo", "C-Max"], "Renault":["Twingo", "Mégane", "Scénic", "Grand Scénic Turbo"]}

bmw = Auto("BMW", "547 T Variant", "Kombi", 170, "Benzin", 650, 298000, 2001, 135000)
fiat = Auto("Fiat", "Multipla", "Kombi", 68, "Benzin", 690, 165300, 1997, 37000)
brabus = Auto("Brabus", "GLS 750 Twin-turbo", "Off-Road", 266, "Benzin", 440, 85000, 2011, 990000)
octavia_1 = Auto("Škoda", "Octavia", "Kombi", 103, "Nafta", 605, 59000, 2020, 475500)
vw_golf = Auto("Volkswagen", "Golf GTI", "Hatchback", 145, "Benzin", 370, 77000, 2014, 515000)
fabia_1 = Auto("Škoda", "Fabia", "Hatchback", 51, "Benzin", 370, 115000, 2014, 129700)
topovka_car_list = [bmw, fiat, brabus, octavia_1, vw_golf, fabia_1]
for gen_car in range(200):
    brand = choice(list(brand_model_dict.keys()))
    model = choice(brand_model_dict[brand])
    chassis = choice(["Kombi", "Hatchback", "Sedan", "Off-Road", "Liftback"])
    output = randint(47, 168)
    fuel = choice(["Benzin", "Nafta", "LPG"])
    if chassis == "Kombi":
        trunk = randint(530, 950)
    elif chassis == "Sedan" or chassis == "Hatchback":
        trunk = randint(240, 400)
    else: trunk = randint(400, 650)
    mileage = randint(10000, 375000)
    year = randint(1985, 2020)
    if mileage < 120000 and year > 2018:
        price = randint(200000, 1250000)
    elif mileage > 250000 and year < 2005:
        price = randint(25000, 90000)
    else: price = randint(90000, 250000)
    gen_car = Auto(brand, model, chassis, output, fuel, trunk, mileage, year, price)
    topovka_car_list.append(gen_car)


#for car in topovka_car_list:
    #print(car)
#print(len(topovka_car_list))