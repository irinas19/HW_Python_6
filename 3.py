#Самая далекая планета


def find_farthest_orbit(orbits):
    max_r = max([a * b for a, b in orbits if a != b])
    r = [(a, b) for a, b in orbits if a * b == max_r]
    return r


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))