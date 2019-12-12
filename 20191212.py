
class Moon():
    def __init__(self, name, x, y, z):
        self.position = (x, y, z)
        self.velocity = (0, 0, 0)
        self.name = name
        self.potential_energy = 0
        self.kinetic_energy = 0
        self.total_energy = 0

    def __str__(self):
        return "{0:10} - pos=<x={1:3}, y={2:3}, z={3:3} > , vel=<x={4:3}, y={5:3}, z={6:3}>, total_energy={7:2}".format(self.name, self.position[0], self.position[1], self.position[2], self.velocity[0], self.velocity[1], self.velocity[2], self.total_energy)

    def calculate_velocity(self, moon_list):
        x_vel = self.velocity[0]
        y_vel = self.velocity[1]
        z_vel = self.velocity[2]
        for moon in moon_list:
            x_vel += compare_position(moon.position[0], self.position[0])
            y_vel += compare_position(moon.position[1], self.position[1])
            z_vel += compare_position(moon.position[2], self.position[2])
        self.velocity = (x_vel, y_vel, z_vel)

    def apply_velocity(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1], self.position[2] + self.velocity[2])

    def calculate_total_energy(self):
        self.potential_energy = sum([abs(p) for p in self.position])
        self.kinetic_energy = sum([abs(p) for p in self.velocity])
        self.total_energy = self.potential_energy * self.kinetic_energy


def compare_position(x_moon, x_self):
    if x_moon < x_self:
        return -1
    elif x_moon > x_self:
        return +1
    else:
        return 0


def run_pgm(moon_list, time):
    #print("Step", 0)
    # for moon in moon_list:
    # print(moon)
    total_energy = 0
    for _ in range(1, time+1):
        #print("Step", t)
        for moon in moon_list:
            moon.calculate_velocity(moon_list)
        for moon in moon_list:
            moon.apply_velocity()
            moon.calculate_total_energy()
            # print(moon)
        total_energy = sum([moon.total_energy for moon in moon_list])
       #print("Sum of total energy : ", )
    return total_energy


if __name__ == "__main__":

    # input :
    # <x=3, y=15, z=8>
    # <x=5, y=-1, z=-2>
    # <x=-10, y=8, z=2>
    # <x=8, y=4, z=-5>

    moon_list = {
        Moon("io", -1, 0, 2),
        Moon("europa", 2, -10, -7),
        Moon("ganymede", 4, -8, 8),
        Moon("callisto", 3, 5, -1)}
    energy = run_pgm(moon_list, 10)
    assert energy == 179

    moon_list = {
        Moon("io", -8, -10, 0),
        Moon("europa", 5, 5, 10),
        Moon("ganymede", 2, -7, 3),
        Moon("callisto", 9, -8, -3)}
    energy = run_pgm(moon_list, 100)
    assert energy == 1940

    # input :
    # <x=3, y=15, z=8>
    # <x=5, y=-1, z=-2>
    # <x=-10, y=8, z=2>
    # <x=8, y=4, z=-5>
    moon_list = {
        Moon("io", 3, 15, 8),
        Moon("europa", 5, -1, -2),
        Moon("ganymede", -10, 8, 2),
        Moon("callisto", 8, 4, -5)}
    energy = run_pgm(moon_list, 1000)
    print(energy)
