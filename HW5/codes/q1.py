import math

class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(d1, d2):
    return math.sqrt((d1.x - d2.x) ** 2 + (d1.y - d2.y) ** 2)

def smallSampleCase(drones):
    min_dist = float('inf')
    n = len(drones)
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(drones[i], drones[j]))
    return min_dist

def stripClosest(strip, d):
    min_val = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y) < min_val:
                min_val = min(min_val, distance(strip[i], strip[j]))
    return min_val

def closestUtil(drones):
    if len(drones) <= 3:
        return smallSampleCase(drones)

    mid = len(drones) // 2
    mid_drone = drones[mid]

    dl = closestUtil(drones[:mid])
    dr = closestUtil(drones[mid:])

    d = min(dl, dr)

    strip = [drone for drone in drones if abs(drone.x - mid_drone.x) < d]

    strip.sort(key=lambda drone: drone.y)

    return min(d, stripClosest(strip, d))

def closestDrones(drones):
    drones.sort(key=lambda drone: drone.x)
    return closestUtil(drones)

# Test cases
test_cases = [
    [Drone(10, 10), Drone(20, 20), Drone(30, 30)],
    [Drone(1, 5), Drone(4, 8), Drone(7, 2), Drone(9, 6)],
    [Drone(3, 3), Drone(17, 9), Drone(4, 15), Drone(8, 7), Drone(15, 3)],
    [Drone(2, 3), Drone(12, 30), Drone(40, 50), Drone(50, 1), Drone(12, 10), Drone(5, 7)]
]

for drones in test_cases:
    print("Test case:")
    print("----------")
    for drone in drones:
        print("Drone at ({}, {})".format(drone.x, drone.y))
    print("Minimum distance:", closestDrones(drones))


