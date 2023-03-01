class Auto:
    def __init__(self, brand, model, chassis, output, fuel, trunk_vol, mileage, year_made, price):
        self.brand = brand
        self.model = model
        self.chassis = chassis
        self.output = output
        self.fuel = fuel
        self.trunk_vol = trunk_vol
        self.mileage = mileage
        self.year_made = year_made
        self.price = price
    def __str__(self):
        return """
        {b} {m} - karoserie: {ch}\n
        výkon {o} kW, palivo: {f}\n
        objem zavazadlového prostoru: {t} l\n
        najeto km: {mi}, rok výroby: {y}\n
        cena: {p},- Kč
        """.format(b = self.brand, m = self.model, ch = self.chassis, o = self.output, f = self.fuel, t = self.trunk_vol, mi = format(self.mileage, ',d').replace(',',' '), y = self.year_made, p = format(self.price, ',d').replace(',',' '))

