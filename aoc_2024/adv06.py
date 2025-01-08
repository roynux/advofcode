class Room:
    def __init__(self, map_data):
        # Initialize the map data and dimensions
        self.map = map_data
        self.height = len(self.map)
        self.width = len(self.map[0])

        # Find the guard position and obstacles
        self.guard = None
        self.obstacles = set()
        self.guard_positions_history = set()
        self.loop_detected = False

        for y in range(self.height):
            for x in range(self.width):
                # Check if the current cell is a guard
                if self.map[y][x] == "^":
                    self.guard = (y, x, "^")  # Guard facing north
                elif self.map[y][x] == "v":
                    self.guard = (y, x, "v")  # Guard facing south
                elif self.map[y][x] == "<":
                    self.guard = (y, x, "<")  # Guard facing west
                elif self.map[y][x] == ">":
                    self.guard = (y, x, ">")  # Guard facing east

                # Check if the current cell is an obstacle
                if self.map[y][x] == "#":
                    self.obstacles.add((y, x))

        self.guard_positions_history.add(self.guard)
        self.guard_inside_map = self.is_guard_inside_map()

    # @property
    def is_guard_inside_map(self):
        return 0 <= self.guard[0] < self.height and 0 <= self.guard[1] < self.width

    @property
    def guard_distinct_positions(self):
        return len(set((y, x) for (y, x, _) in self.guard_positions_history)) - 1

    def step(
        self,
    ):  # Move the guard based on its direction. If the new position is an obstacle, turn right instead of moving.
        if self.guard[2] == "^":
            new_y = self.guard[0] - 1
            new_x = self.guard[1]
        elif self.guard[2] == "v":
            new_y = self.guard[0] + 1
            new_x = self.guard[1]
        elif self.guard[2] == "<":
            new_y = self.guard[0]
            new_x = self.guard[1] - 1
        elif self.guard[2] == ">":
            new_y = self.guard[0]
            new_x = self.guard[1] + 1
        # Check if the new position is an obstacle
        if (new_y, new_x) in self.obstacles:
            # Turn right instead of moving
            if self.guard[2] == "^":
                self.guard = (self.guard[0], self.guard[1], ">")
            elif self.guard[2] == "v":
                self.guard = (self.guard[0], self.guard[1], "<")
            elif self.guard[2] == "<":
                self.guard = (self.guard[0], self.guard[1], "^")
            elif self.guard[2] == ">":
                self.guard = (self.guard[0], self.guard[1], "v")
        else:
            # Move to the new position
            self.guard = (new_y, new_x, self.guard[2])
        self.loop_detected = self.guard in self.guard_positions_history
        self.guard_positions_history.add(self.guard)
        self.guard_inside_map = self.is_guard_inside_map()


def part1(adv06_data):
    room = Room(adv06_data)
    count = 0
    while room.guard_inside_map and count < 100000:
        room.step()
        count += 1
    print(
        f"Part 1: {count} steps, number of distinct positions: {room.guard_distinct_positions}"
    )


def detect_loop_in_room(map_data, new_obstacle_y, new_obstacle_x):
    room = Room(map_data)

    if (new_obstacle_y, new_obstacle_x) in room.obstacles:
        return False

    room.obstacles.add((new_obstacle_y, new_obstacle_x))

    count = 0
    while room.guard_inside_map and (room.loop_detected is False) and count < 1000000:
        room.step()
        count += 1

    return room.loop_detected


def part2(adv06_data):
    loop_positions = []
    for y in range(len(adv06_data)):
        print(f"Detecting loop at line {y}...")
        for x in range(len(adv06_data[0])):
            if adv06_data[y][x] == ".":
                if detect_loop_in_room(adv06_data, y, x):
                    loop_positions.append((y, x))
    return len(loop_positions)


# main function call part1
if __name__ == "__main__":
    # load content of file adv06.txt
    with open("aoc_2024/adv06.txt", "r") as f:
        adv06_data = f.readlines()
    part1(adv06_data)
    print(f"Nbr of different obstacle positions: {part2(adv06_data)}.")
