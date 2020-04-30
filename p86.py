class Consumer:
    def ___init___(self, w):
        self.wealth = w

    def earn(self, y):
        self.wealth = self.wealth + y

    def spend(self, x):
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("insufficent funds")
        else:
            self.wealth = new_wealth

