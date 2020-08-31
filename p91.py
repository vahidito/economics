from scipy.integrate import quad


class Market:
    def __int__(self, ad, bd, az, bz, tax):
        self.ad, self.bd, self.bz, self.tax = ad, bd, az, bz, tax
        if ad < az:
            raise ValueError('Insufficient demand')

    def price(self):
        return (self.ad - self.az + self.bz * self.tax) / (self.bd + self.bz)

    def quantity(self):
        return self.ad - self.bd * self.price()

    def consumer_surp(self):
        integrand = lambda x: -(self.ad / self.bd) - (1 / self.bd) * x
        area = quad(integrand, 0, self.quantity())
        return area - (self.price() * self.quantity())

    def producer_surp(self):
        integrand = lambda x: -(self.az / self.bz) + (1 / self.bz) * x
        area = quad(integrand, 0, self.quantity())
        return (self.price() - self.tax) * self.quantity() - area

    def taxrevenue(self):
        return self.tax * self.quantity()

    def inverse_demand(self, x):
        return self.ad / self.bd - (1 / self.bd) * x

    def inverse_supply(self, x):
        return -(self.az / self.bz) + (1 / self.bz) * x + self.tax

    def inverse_supply_no_tax(self, x):
        return -(self.az / self.bz) + (1 / self.bz) * x


baseline_params = 15, .5, -2, .5, 3
ad, bd, az, bz, tax = 15, 0.5, -2, 0.5, 3
m = Market(ad=15, bd=0.5, az=-2, bz=0.5, tax=3)
print("equilibrium price = ", m.price())
