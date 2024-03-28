import matplotlib.pyplot as plt
import math


class Sensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Sensor({self.x}, {self.y})"


def isRightTurn(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) < 0


def convexHull(sensors):
    if len(sensors) < 3:
        return sensors

    bottom_left = min(sensors, key=lambda s: (s.y, s.x))
    sensors.remove(bottom_left)

    sensors.sort(key=lambda p: (math.atan2(p.y - bottom_left.y, p.x - bottom_left.x), p.y, p.x))
    sensors = [bottom_left] + sensors

    hull = []
    for sensor in sensors:
        while len(hull) >= 2 and isRightTurn(hull[-2], hull[-1], sensor):
            hull.pop()
        hull.append(sensor)

    return hull


# Test cases
test_sets = [
    [Sensor(0, 0), Sensor(1, 1), Sensor(0, 2), Sensor(2, 2), Sensor(3, 1), Sensor(2, 0), Sensor(1, -1)],
    [Sensor(1, 2), Sensor(3, 4), Sensor(5, 1), Sensor(6, 3), Sensor(4, 5), Sensor(2, 3)],
    [Sensor(-2, 0), Sensor(-1, 2), Sensor(0, 0), Sensor(1, -2), Sensor(-1, -3), Sensor(2, 1)]
]

# Plot the sensors and convex hull for each test set
for i, sensors in enumerate(test_sets):
    hull_sensors = convexHull(sensors)

    sensor_x = [s.x for s in sensors]
    sensor_y = [s.y for s in sensors]
    hull_x = [s.x for s in hull_sensors] + [hull_sensors[0].x]
    hull_y = [s.y for s in hull_sensors] + [hull_sensors[0].y]

    plt.figure()
    plt.scatter(sensor_x, sensor_y, color='blue')
    plt.plot(hull_x, hull_y, color='red')
    plt.fill(hull_x, hull_y, color='red', alpha=0.3)
    plt.title(f'Test Set {i + 1}: Sensors and Convex Hull')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()

    print(f"Test Set {i + 1}: Sensors forming the convex hull:", hull_sensors)