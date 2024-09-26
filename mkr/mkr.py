import matplotlib.pyplot as plt
import numpy as np

xw, yw, st = 1000, 1000, 50
dx, dy = 10, 10
rect_width = 3 * st
rect_height = st

fig, ax = plt.subplots()
plt.xlim(0, xw)
plt.ylim(0, yw)
ax.set_aspect('equal')
x1 = (xw - rect_width) / 2
y1 = (yw - rect_height) / 2
x2 = x1 + rect_width
y2 = y1 + rect_height

rect = plt.Rectangle((x1, y1), rect_width, rect_height, edgecolor='blue', facecolor='none')
ax.add_patch(rect)
plt.draw()
plt.pause(1)

for i in range(int(xw / st)):
    rect.set_edgecolor('white')
    x1 -= dx
    y1 -= dy
    x2 += dx
    y2 += dy
    rect = plt.Rectangle((x1, y1), x2-x1, y2-y1, edgecolor='blue', facecolor='none')
    ax.add_patch(rect)
    plt.draw()
    plt.pause(0.1)

plt.show()


fig, ax = plt.subplots()
plt.xlim(0, xw)
plt.ylim(0, yw)
ax.set_aspect('equal')
dx, dy = 50, 50
width, height = 80, 40
angle = np.radians(10)

x1, y1 = 50, yw - 50
x2, y2 = x1 + width, y1
x3, y3 = x2, y1 - height
x4, y4 = x1, y3

square = plt.Polygon([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], edgecolor='blue', facecolor='none')
ax.add_patch(square)
plt.draw()
plt.pause(1)


for i in range(100):
    square.set_edgecolor('white')
    center_x = (x1 + x3) / 2 + dx
    center_y = (y1 + y3) / 2 + dy

    vertices_matrix = np.array([[x1, y1, 1],
                                [x2, y2, 1],
                                [x3, y3, 1],
                                [x4, y4, 1]])

    translation_matrix = np.array([[1, 0, -center_x],
                                   [0, 1, -center_y],
                                   [0, 0, 1]])

    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])

    reverse_translation_matrix = np.array([[1, 0, center_x],
                                           [0, 1, center_y],
                                           [0, 0, 1]])

    transformation_matrix = reverse_translation_matrix.dot(rotation_matrix).dot(translation_matrix)
    updated_vertices = vertices_matrix.dot(transformation_matrix.T)

    x1, y1, _ = updated_vertices[0]
    x2, y2, _ = updated_vertices[1]
    x3, y3, _ = updated_vertices[2]
    x4, y4, _ = updated_vertices[3]

    square = plt.Polygon([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], edgecolor='blue', facecolor='none')
    ax.add_patch(square)
    plt.draw()
    plt.pause(0.1)

plt.show()
