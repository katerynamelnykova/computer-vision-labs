from graphics import *
import time
import math as mt

#----------------              I. TRANSLATION                        ------------------------
#---------------- forming a static hexagon                            ------------------------

xw=600; yw=600; st=50                         # dimensions of the graphic window and transformation parameters
dx = 50; dy = 50
# dimensions of the hexagon
x1=st; y1=yw-st
x2=2*st; y2=yw-2*st
x3=3*st; y3=yw-st
x4=3*st; y4=yw
x5=2*st; y5=yw+st
x6=st; y6=yw

#------------------------ Cyclic translation using scalar operations -----------------------
win = GraphWin("2-D geometric transformations TRANSLATION", xw, yw)
win.setBackground('white')

x_list = [x1, x2, x3, x4, x5, x6]
y_list = [y1, y2, y3, y4, y5, y6]

x_list_moved = [x + dx for x in x_list]
y_list_moved = [y - dy for y in y_list]

points_moved = [Point(x, y) for x, y in zip(x_list_moved, y_list_moved)]
obj = Polygon(*points_moved)
obj.draw(win)

stop = xw / dx
stop = float(stop)
ii = int(stop)
for i in range(ii):
    time.sleep(0.3)
    obj.move(dx, -dy)

win.getMouse()
win.close()

#----------------              II. ROTATION                        ------------------------

win = GraphWin("2-D geometric transformations ROTATION", xw, yw)
win.setBackground('white')

# Coordinates of the hexagon vertices
hexagon_points = [
    Point(300, 300), Point(350, 300), Point(400, 350),
    Point(350, 400), Point(300, 400), Point(250, 350)
]

# Drawing the initial hexagon
hexagon = Polygon(*hexagon_points)
hexagon.draw(win)

# Initial rotation angle (in radians)
angle_rad = 0

# Loop for rotation animation
for i in range(72*3): # making 3 full rotations
    # Delay for smooth animation
    time.sleep(0.05)

    # Clear the previous hexagon
    hexagon.undraw()

    # Update the rotation angle
    angle_rad += mt.pi / 36  # Rotate by 5 degrees (or pi/36 radians)

    # Calculate new coordinates of the hexagon vertices after rotation
    new_hexagon_points = []
    for point in hexagon_points:
        # Calculate new coordinates for each vertex
        rotated_x = (point.getX() - 350) * mt.cos(angle_rad) - (point.getY() - 350) * mt.sin(angle_rad) + 350
        rotated_y = (point.getX() - 350) * mt.sin(angle_rad) + (point.getY() - 350) * mt.cos(angle_rad) + 350
        new_hexagon_points.append(Point(rotated_x, rotated_y))

    # Draw the new hexagon
    hexagon = Polygon(*new_hexagon_points)
    hexagon.draw(win)

# Wait for mouse click to close the window
win.getMouse()
win.close()


#----------------              III. SCALING                        ------------------------

win = GraphWin("2-D geometric transformations SCALING", xw, yw)
win.setBackground('white')

# Coordinates of the hexagon vertices
hexagon_points = [
    Point(250, 350), Point(300, 300), Point(350, 300),
    Point(400, 350), Point(350, 400), Point(300, 400)
]

# Drawing the initial hexagon
hexagon = Polygon(*hexagon_points)
hexagon.draw(win)

# Initial scale
scale_factor = 1.0

# Find the center of the hexagon
center_x = sum(point.getX() for point in hexagon_points) / 6
center_y = sum(point.getY() for point in hexagon_points) / 6

# Loop for scaling animation
for i in range(100):
    # Delay for smooth animation
    time.sleep(0.05)

    # Clear the previous hexagon
    hexagon.undraw()

    # Increase the scale
    scale_factor += 0.02

    # Calculate new coordinates of the hexagon vertices after scaling
    new_hexagon_points = []
    for point in hexagon_points:
        # Calculate the distance from each vertex to the center
        dx = point.getX() - center_x
        dy = point.getY() - center_y

        # Scale the distance from the center
        scaled_dx = dx * scale_factor
        scaled_dy = dy * scale_factor

        # New coordinates of the vertex
        new_x = center_x + scaled_dx
        new_y = center_y + scaled_dy

        new_hexagon_points.append(Point(new_x, new_y))

    # Draw the new hexagon
    hexagon = Polygon(*new_hexagon_points)
    hexagon.draw(win)

# Wait for mouse click to close the window
win.getMouse()
win.close()
