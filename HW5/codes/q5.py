class Antenna:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Antenna({self.start}, {self.end})"

def activate_antennas(antennas):
    # Sort the antennas by their end points
    antennas.sort(key=lambda x: x.end)

    activated = []
    current_end = -float('inf')

    for antenna in antennas:
        if antenna.start > current_end:
            activated.append(antenna)
            current_end = antenna.end

    return activated

# Test Cases
antennas = [Antenna(1, 4), Antenna(2, 3), Antenna(5, 8), Antenna(6, 7)]
activated_antennas = activate_antennas(antennas)

antennas_list = [[Antenna(1, 4), Antenna(2, 3), Antenna(5, 8), Antenna(6, 7)],
                 [Antenna(1, 2), Antenna(3, 4), Antenna(5, 6), Antenna(7, 8)],
                 [Antenna(1, 8), Antenna(2, 7), Antenna(3, 6), Antenna(4, 5)]]
activated_antennas_list = [activate_antennas(antennas) for antennas in antennas_list]

for antennas, activated_antennas in zip(antennas_list, activated_antennas_list):
    print("Test case:")
    print("----------")
    print("Antennas:", antennas)
    print("Activated Antennas:", activated_antennas)
