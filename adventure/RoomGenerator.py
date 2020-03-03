import random

# Merchant to go here
CHARACTER_TILES = "MERCHANT"

class Generator():

    #width to be decided, height to be decided these are placeholders
    def __init__(self, width = 64, height = 64, max_rooms = 100, min_room_xy = 100,
                 max_room_xy = 10, rooms_overlap = False, random_connections = 1, tiles = CHARACTER_TILES):


       self.width = width
       self.height = height
       self.max_rooms = max_rooms
       self.min_room_xy = min_room_xy
       self.max_room_xy = max_room_xy
       self.rooms_overlap = rooms_overlap
       self.random_connections = random_connections
       self.tiles = CHARACTER_TILES
       self.level = []
       self.room_list = []
       self.corridor_list = []
       self.tiles_level = []



    def generate_room(self):
        x, y, w, h = 0, 0, 0, 0

        w = random.randint(self.min_room_xy, self.max_room_xy)
        h = random.randint(self.min_room_xy, self.max_room_xy)
        x = random.randint(1, (self.width - w - 1))
        y = random.randint(1, (self.height - h - 1))

        return [x, y, w, h]






if __name__ == '__main__':
    gen = Generator()
    # gen.gen_level()
    # gen.gen_tiles_level()
