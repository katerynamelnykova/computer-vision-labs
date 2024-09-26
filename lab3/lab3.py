import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Coordinates of a pyramid with a quadrilateral base
st, height, offset = 1000, 800, 300
Pyramid = np.array([
    [0, 0, 0, 1],
    [st, 0, 0, 1],
    [st + offset, st, 0, 1],
    [0 + offset, st, 0, 1],
    [st / 2 + offset / 2, st / 2, height, 1]  # Apex of the pyramid
])

# Projection function onto xy
def ProjectXY(Figure):
    f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    return Figure.dot(f.T)

# Shifting
def ShiftXYZ(Figure, l, m, n):
    f = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [0, 0, 0, 1]])
    return Figure.dot(f.T)

# Axonometry
def dimetri(Figure, TetaG1, TetaG2):
    TetaR1, TetaR2 = np.radians(TetaG1), np.radians(TetaG2)
    f1 = np.array([[np.cos(TetaR1), 0, -np.sin(TetaR1), 0], [0, 1, 0, 0], [np.sin(TetaR1), 0, np.cos(TetaR1), 1], [0, 0, 0, 0]])
    f2 = np.array([[1, 0, 0, 0], [0, np.cos(TetaR2), np.sin(TetaR2), 0], [0, -np.sin(TetaR2), np.cos(TetaR2), 0], [0, 0, 0, 1]])
    return Figure.dot(f1.T).dot(f2.T)

# Visualization of the pyramid with Lagrange interpolation
def PyramidWiz(Prxy):
    base_vertices = Prxy[:4]
    apex = Prxy[4]
    vertices = np.vstack((base_vertices, base_vertices[0]))  # Closing the base

    # Building pyramid sides with Lagrange interpolation
    for i in range(4):
        x = [base_vertices[i, 0], apex[0]]
        y = [base_vertices[i, 1], apex[1]]
        poly = lagrange(x, y)
        x_new = np.linspace(x[0], x[1], 100)
        y_new = poly(x_new)
        plt.plot(x_new, y_new, 'b-')

    # Building the base of the pyramid
    plt.plot(vertices[:, 0], vertices[:, 1], 'ro-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Pyramid with Lagrange interpolation')
    plt.grid(True)
    plt.show()

xw, yw, st, TetaG1, TetaG2 = 600, 600, 50, 0, 100
l, m, n = (xw / 2) - st, (yw / 2) - st, st
Pyramid1 = ShiftXYZ(Pyramid, l, m, n)
Pyramid2 = dimetri(Pyramid1, TetaG1, TetaG2)
Prxy3 = ProjectXY(Pyramid2)
PyramidWiz(Prxy3)
