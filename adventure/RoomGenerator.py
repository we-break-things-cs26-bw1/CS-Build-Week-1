class Rectangle:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h


    def create_room(room):
        global map
        for x in range(room.x1, room.x2 + 1 ):
            for y in range(room.y1, room.y2 + 1):
                map[x][y].blocked = False
                map[x][y].block_sight = False


