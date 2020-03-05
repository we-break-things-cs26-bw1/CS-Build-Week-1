import random, math


# https://unminify.com/ Unminified, each string is a 3x3 grid of corridors and walls.
# I've set up 15 rooms, totalling all combinations of walls/corridors without corridors in the corners.
room_templates = [
    " ■  ■  ■ ",
    "   ■■■   ",
    "    ■■ ■ ",
    "   ■■  ■ ",
    " ■  ■■   ",
    " ■ ■■    ",
    "   ■■■ ■ ",
    " ■  ■■ ■ ",
    " ■ ■■■   ",
    " ■ ■■  ■ ",
    " ■ ■■■ ■ ",
    "    ■  ■ ",
    "    ■■   ",
    " ■  ■    ",
    "   ■■   "
]
corridor, wall = "■ "
null_room = wall * 9

# constants for room slicing/printing
top, middle, bottom = [slice(3), slice(3, 6), slice(6, 9)]
room_parts = [top, middle, bottom]

# constants for each direction
directions = North, West, East, South = 1, 3, 5, 7
opposite = {North: South, East: West, South: North, West: East}
offset = {
    North: lambda x, y: (x, y - 1),
    East: lambda x, y: (x + 1, y),
    South: lambda x, y: (x, y + 1),
    West: lambda x, y: (x - 1, y)
}

# Stores the generated rooms sparsely for memory reasons.
# Keys are tuples of form (x,y), values are room strings.
# Coordinates begin from the top left.
dungeon = {}


def get_room(x, y): return dungeon.get((x, y), null_room)


# The maximum size of the grid. Generation will start in the middle.
# 17x9 generates a roughly visually square grid, can be made anything
maxx, maxy = 20, 20


# === Random Generation and Room Handling === #

# Picks a random room with the given connections.
def random_room(*connections, only=False):
    if only:
        l = list(filter(
            lambda r: has_connections(r, *connections) and set(get_connections(r)) == set(connections), room_templates))
        return l[0] if len(l) > 0 else null_room
    else:
        return random.choice(list(filter(lambda r: has_connections(r, *connections), room_templates)))


# Returns true if the given room has all the given connections.
def has_connections(room, *connections):
    return all(room[c] == corridor for c in connections)


# Returns a list of connections for the given room.
def get_connections(room, ideal=False):
    return [c for c in directions if has_connections(room, c)]


# Returns a list of connections the given room should have from context.
def get_connections_list_context(x, y):
    return [dir for dir in directions if has_connections(get_room(*offset[dir](x, y)), opposite[dir])]


# Generates a random dungeon by recursively generating a room at each coordinate.
def gen_room(x, y, first=True):
    if x not in range(maxx) or y not in range(maxy): return
    if (x, y) in dungeon: return

    if first:
        print("Generating first room at " + str((x, y)) + "...")
        dungeon[(x, y)] = random.choice(room_templates)
    else:
        connections = get_connections_list_context(x, y)
        if len(connections) < 1: return False
        print("Generating room at " + str((x, y)) + "...")
        dungeon[(x, y)] = random_room(*connections)

    [gen_room(*offset[dir](x, y), False) for dir in get_connections(dungeon[(x, y)])]
    return True


# Entry point for dungeon generation and cleanup of unwanted dead ends and prints the output.
def gen_dungeon():
    print("Beginning dungeon generation...")
    gen_room(int(math.floor(maxx / 2)), int(math.floor(maxy / 2)))

    print("connections exhausted.")
    print("cleaning up unwanted dead ends...")
    for x in range(maxx):
        for y in range(maxy):
            dungeon[(x, y)] = random_room(*get_connections_list_context(x, y), only=True)
    print("Finished dungeon generation!")

    print_grid()



# Prints a row of rooms from the grid.
def print_row(y):
    [[print("|", end=""), [print(get_room(x, y)[part], end="|") for x in range(maxx)], print("")] for part in
     room_parts]


# Prints the entire grid.
def print_grid():
    print("----" * maxx + "-")
    [[print_row(y), print("----" * maxx + "-")] for y in range(maxy)]


# === Main Function === #
if __name__ == "__main__": gen_dungeon()
