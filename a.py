from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import matplotlib.patches as mpatches
class sinif():
    def __init__(self):
        self.x_data, self.y_data = [], []
        self.figure = pyplot.figure(figsize=(16,8))
        pyplot.xlim(0,500)
        self.i=1
        self.line, = pyplot.plot(self.x_data, self.y_data, '-')
        self.animation = FuncAnimation(self.figure, self.update, interval=200)
        pyplot.show()

    def update(self, frame):
        print(self.i)
        self.i+=1
        self.x_data.append(randrange(1*(self.i*2),(10*(self.i*2))))
        self.y_data.append(randrange(0, 100))
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,


if __name__ == "__main__":
    program = sinif()