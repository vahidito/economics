import matplotlib.pyplot as plt


class Chaos:
    def __init__(self, x, r):
        self.x, self.r = x, r

    def update(self):
        self.x = self.r * self.x * (1 - self.x)

    def generate_seq(self, n):
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path


ch = Chaos(0.1, 4.0)
ts_length = 100
fig, ax = plt.subplots()
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$x_t$', fontsize=14)
x = ch.generate_seq(ts_length)
#print(x)
#ax.plot(range(ts_length), x, 'bo-', alpha=0.5, lw=2, label='$x_t$')
#plt.show()

fig, ax = plt.subplots()
ch1 = Chaos(0.1, 4)
r = 2.5
while r < 4:
    ch1.r = r
    t = ch.generate_seq(1000)[950:]
    ax.plot([r] * len(t), t, 'b.', ms=0.6)
    r = r + 0.005
ax.set_xlabel('$r$', fontsize=16)
plt.show()