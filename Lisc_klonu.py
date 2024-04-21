import matplotlib.pyplot as plt
import random as rnd

x = [0]
y = [0]

def apply_transformation(x, y, p):
    if p < 0.1:
        new_x = 0.14*x + 0.01*y - 1.31
        new_y = 0.0*x + 0.51*y + 0.1
    elif p < 0.45:
        new_x = 0.43*x + 0.52*y + 1.49
        new_y = -0.45*x + 0.5*y - 0.75
    elif p < 0.8:
        new_x = 0.45*x - 0.49*y - 1.62
        new_y = 0.47*x + 0.47*y - 0.74
    else:
        new_x = 0.49*x + 0.0*y + 0.02
        new_y = 0.0*x + 0.51*y + 1.62
    return new_x, new_y

for i in range(1, 1000000):
    try:
        p = rnd.random()
        new_x, new_y = apply_transformation(x[i-1], y[i-1], p)
        x.append(new_x)
        y.append(new_y)
    except IndexError:
        print("Index error")

plt.plot(x, y, ".", markersize=0.1)
plt.show()
