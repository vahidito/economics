class Solow:
    def __init__(self, n=0.02, s=0.25, delta=0.1, alpha=0.3, z=2.0, k=1.0):
        self.n, self.s, self.delta, self.alpha, self.z = n, s, delta, alpha, z
        self.k = k

    def h(self):
        n, s, delta, alpha, z = self.n, self.s, self.delta, self.alpha, self.z
        return (s * z * self.k ** alpha + (1 - delta) * self.k) / (1 + n)

    def update(self):
        self.k = self.h()

    def steady_state(self):
        n, s, delta, alpha, z = self.n, self.s, self.delta, self.alpha, self.z
        return ((s * z) / (n + delta)) ** (1 / (1 - alpha))
