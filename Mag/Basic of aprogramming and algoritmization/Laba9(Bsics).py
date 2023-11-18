import math as ma
import matplotlib.pyplot as plt

class Ball:

    def __init__(self, alpha, v0, coordinat=(0.0, 0.0), timeSettings=(0, 1, 1e-1)):
        self.coord = coordinat
        self.alpha = alpha
        self.v0 = v0
        self.g = 9.8
        self.acceleration = 4
        self.timeSettings = timeSettings

    def generateTime(self):
        t0 = self.timeSettings[0]
        t_end = self.timeSettings[1]
        delta_t = self.timeSettings[2]

        self.time = [t0]  # refresh times

        while self.time[-1] <= t_end:
            self.time.append(self.time[-1] + delta_t)

    def calcCoord(self):
        self.x = []
        self.y = []

        if self.v0 * ma.cos(self.alpha) > 0:
            a = -self.acceleration
        elif self.v0 * ma.cos(self.alpha) == 0:
            a = 0
        else:
            a = self.acceleration

        self.generateTime()
        for t in self.time:
            self.x.append(self.coord[0] + self.v0 * ma.cos(self.alpha) + 0.5 * a * t ** 2)
            self.y.append(self.coord[0] + self.v0 * ma.sin(self.alpha) - 0.5 * self.g * t ** 2)

    def plotCoord(self):

        plt.plot(self.time, self.x, label=f'x-coord {self.alpha / ma.pi * 180}')
        plt.plot(self.time, self.y, label=f'x-coord {self.alpha / ma.pi * 180}')
        plt.legend()


alpha = ma.pi / 6
v0 = 10
ball = Ball(alpha, v0)
ball.calcCoord()
ball.plotCoord()

for alpha in [ma.pi / 10, ma.pi / 6, ma.pi / 3, ma.pi / 2]:
    ball = Ball(alpha, v0)
    ball.calcCoord()
    ball.plotCoord()

