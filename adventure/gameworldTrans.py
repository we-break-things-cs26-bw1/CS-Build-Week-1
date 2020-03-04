

#  this is an imply of munificient's beautiful maze algo from:
#  we went through... a lot of maze algos and this one actually produces stuff
# that looks sort of real instead of boxy or mazey...
#dart code to be translated can be found on the repo,
# hopefully my notes indicate the progress I've made so
#far translating it. GOOD LUCK FRIEND, SEE YOU THURSDAY.
# https://github.com/munificent/hauberk/blob/db360d9efa714efb6d937c31953ef849c7394a39/lib/src/content/dungeon.dart


# pos are 2 Tuple

# stage is the global play area

## stage.dart should be complete, including stage class, tile and tiletypes.
##some code was omited because it references features we will not have, such as
## movable actors besides the player.

# stage builder.dart is almost one for one translated into this file, should be compolet

# I am leaving off for the night at onDecorateRooms()/ _growmaze()
# on decorate room I believe can be avoided for now and just _growMaze is next
# much of the remaining code is quite reasonable, I'm just exhausted.lol
## also the list that follows has some call outs for stuff we need to finish this port,
# mostly rect/vec classes and methods... shouldn't be too painful


## what remains?
##
##dungeon.dart
## Rect/vec classes and methods
## RECT NEEDS INFLATE METHOD
##rng.vecInRect(bounds) == we need a function that returns a vec within a rect
##i.e, it needs to return a random (x,y) tuple within the bounds of our map
# neeed a 1 in x return true function, i.e 1 in 3, roll a rng number, if 1 return true
# self.stage.bounds.height -- bounds off rect needs to be able to provide height
# and width self.stage.bounds.width

import pygame

# heh stupid helper function
def twoTupleAdd(tuple1, tuplle2):
    return (tuple1[0] + tuplle2[0], tuple1[1] + tuplle2[1])


def Array2d(width, height):
    return [[0] * width] * height


Directions = [
    (0, 0),
    (0, -1),  # n
    (0, -1),
    (1, 1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
]

class Vec():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __getattr__(self):
        return (self.x,self.y)


class Stage():
    def __init__(self, tiles, width, height, bounds, items: dict, _numExplorable, _visibilityDirty=True, ):
        """
        :type bounds: Rect (0,0), (9,9)
        :type tiles: 2darray
        :type items: dict (0,0):Items
        :type _numExplorabl: int
        """
        self.tiles = [[0 for j in range(height)] for i in range(width)]
        self.width = width
        self.height = height
        self.bounds = bounds
        self.tiles = tiles
        self.items = {}  # items
        self._visibilityDirty = _visibilityDirty
        self._numExplorable = _numExplorable
        self.rect = pygame.Rect

    def __getitem__(self, pos):
        """"
        :return Tile
        :type pos:Vector (0,0)
        """
        if pos in self.tiles:
            return self.tiles[pos]
        # tiles as map

    def __setitem__(self, key, value):

        self.tiles[key] = value

    """
    /// Called after the level generator has finished laying out the stage.
    """
    """"
      // Count the explorable tiles. We assume the level is fully reachable, so
     // any traversable tile or tile next to a traversable one is explorable.
     """

    def finishBuild(self):
        self._numExplorable = 0

        # inflate method should shrink rect tangle
        # Rect inflate(double delta) {
        #   return Rect.fromLTRB(left - delta, top - delta, right + delta, bottom + delta);
        #    }

        #Takes in an x and a y, uses the center to inflate
        #  inflate() returns a new rect while inflate_ip() modifies the rect you pass it
        self.rect.inflate(self, )

        for pos in self.bounds.inflate(-1):
            tile: Tile = self[pos]
            if tile.isTraversable:
                self._numExplorable += 1
            else:
                for dir in Directions:
                    # debug
                    print(f"resulting dir is {dir}")
                    resultingTuple = (  )
                    if self[resultingTuple].isTraversable:
                        self._numExplorable += 1
                        break

    def itemAt(self, pos):
        """"

        :type pos:Vec
        """
        if self.items.keys():
            return self.items[pos]
        else:
            return None

    # TODO?
    def spawnMonster(self):
        return "Monster here"


class TileType():
    def __init__(self, name, isPassable, isTraversable, appearance, opensTo=None, closesTo=None, isTransparent=False):
        self.name = name
        self.isPassable = isPassable
        self.isTraversable = isTraversable
        self.appearance = appearance
        self.opensTo = opensTo
        self.closesTo = closesTo
        self.isTransparent = isTransparent


class Tile():
    def __init__(self, type: TileType = None, isTraversable=None, appearance=None, visible=False, opensTo=None,
                 closesTo=None, isExplored=False, stage=None):
        """"
        :type pos: Tuple (0,0)
        """
        self.type = type
        self.visible = visible
        self.isTraversable = isTraversable
        self.appearance = appearance
        self.isExplored = isExplored
        self.stage = stage

    def isPassable(self):
        return self.type.isPassable

    def isTraversable(self):
        return self.type.isPassable or (self.type.opensTo)

    def isTransparent(self):
        return self.type.isTransparent


Floor = "Floor"
Wall = "Wall"
TileTypeMap = {}
TileTypeMap[Floor]: TileType(name="floor", isPassable=True, isTraversable=True, appearance="gray"),
TileTypeMap[Wall] = TileType(name="wall", isPassable=False, isTraversable=False, appearance="gray")


class StageBuilder():

    def bindStage(self, stage: Stage):
        self.stage = stage

    def __init__(self, stage: Stage):
        self.stage = stage

    def getTile(self, pos):
        return self.stage[pos]

    def setTile(self, pos, tile):
        self.stage[pos] = tile

    def fill(self, tile: TileType):
        for y in range(self.stage.height):
            for x in range(self.stage.width):
                self.setTile((x, y), tile)

    # /// Randomly turns some [wall] tiles into [floor] and vice versa.
    def erode(self, iterations):
        floor = TileTypeMap[Floor]
        wall = TileTypeMap[Wall]
        # INFLATE METHOD
        bounds = self.stage.bounds.inflate
        for i in range(iterations):
            #      // TODO: This way this works is super inefficient. Would be better to
            #    // keep track of the floor tiles near open ones and choose from them.
            pos = rng.vecInRect(bounds)
            current: Tile = self.getTile(pos)

            if current is not wall:
                continue
            # continue brings us back to the begining of the loop if this pos is not a wall
            # // Keep track of how many floors we're adjacent too. We will only erode
            # // if we are directly next to a floor.
            floors = 0
            for dir in Directions:
                tile = self.getTile(twoTupleAdd(pos, dir))
                if tile is floor: floors += 1
            #      // Prefer to erode tiles near more floor tiles so the erosion isn't too
            #     // spiky.
            if floors < 2: continue

            ####### NEED ONE IN X CODE HERE !!!!!!@!@@!@ TODO()
            if random.oneIn(9 - floors): self.setTile(pos, floor)


class dungeon(StageBuilder):

    def __init__(self, numRoomTries, extraConnectorChance, roomExtraSize, windingPercent, _rooms, _regions,
                 _currrentRegion=-1, stage=None):
        self.numRoomTries = numRoomTries
        # positive int
        # /// The inverse chance of adding a connector between two regions that have
        # /// already been joined. Increasing this leads to more redundantly connected
        # /// dungeons.
        self.extraConnectorChance = extraConnectorChance
        # percentage i.e 20/100
        #  /// Increasing this allows rooms to be larger.
        self.roomExtraSize = roomExtraSize
        ##allows rooms to be larger, int
        self.windingPercent = windingPercent
        # int/100
        self._rooms = _rooms
        # <rect>[]
        self._regions = _regions
        # 2d Array of ints
        # for each open position in the dungeon, the index of the connected region that that position is part of
        #  /// The index of the current region being carved.
        self.currentRegion = _currrentRegion
        self.stage = stage

    def generate(self, stage: Stage):
        if stage.width % 2 == 0 or stage.height % 2 == 0:
            raise ValueError("the stage be odd-sized")
        self.bindStage(stage)
        self.fill(TileTypeMap[Wall])
        self._regions = Array2d(stage.width, stage.height)
        self._addRooms()

        #  // Fill in all of the empty space with mazes.
        # state at 1, increment by 2 to the height of the bounds -w
        for y in range(1, self.stage.bounds.height, 2):
            for x in range(1, self.stage.bounds.width, 2):
                pos = (x, y)
                if self.getTile(pos) is not TileTypeMap[Wall]: continue
                self._growMaze(pos)

        self._connectRegions();
        self._removeDeadEnds();


        #think you might be able to cut this, not sure, definitely review before impl TODO()
        self._rooms.forEach(onDecorateRoom);


##  /// Implementation of the "growing tree" algorithm from here:
# /// http://www.astrolog.org/labyrnth/algrithm.htm.
    def _growMaze(self, start: Vec):
        pass


#    // Find all of the tiles that can connect two (or more) regions.
    def _connectRegions(self):
        pass


    def _removeDeadEnds(self):
        pass


    def _addJunction(self,pos: Vec):
        pass


    def _carve(self,pos, tileType):
        pass


    #   /// Places rooms ignoring the existing maze corridors.
    def _addRooms(self):
        pass


    def setTile(self, TileType):
        pass

# /// Static class containing all of the [TileType]s.
# class Tiles {
#   static TileType floor;
#   static TileType wall;
#   static TileType lowWall;
#   static TileType table;
#   static TileType openDoor;
#   static TileType closedDoor;
#   static TileType stairs;
#
#   static TileType grass;
#   static TileType tree;
#   static TileType treeAlt1;
#   static TileType treeAlt2;
#
#   static void initialize() {
#     // Define the tile types.
#     Tiles.floor = new TileType("floor", true, true,
#         [gray('.'), darkGray('.')]);
#
#     Tiles.wall = new TileType("wall", false, false,
#         [lightGray('#', Color.darkGray), darkGray('#')]);
#
#     Tiles.table = new TileType("table", false, true, [
#       brown(CharCode.greekSmallLetterPi),
#       darkBrown(CharCode.greekSmallLetterPi)
#     ]);
#
#     Tiles.lowWall = new TileType("low wall", false, true,
#         [gray('%', Color.darkGray), darkGray('%')]);
#
#     Tiles.openDoor = new TileType("open door", true, true,
#         [brown("'"), darkBrown("'")]);
#     Tiles.closedDoor = new TileType("closed door", false, false,
#         [brown('+'), darkBrown('+')]);
#     Tiles.openDoor.closesTo = Tiles.closedDoor;
#     Tiles.closedDoor.opensTo = Tiles.openDoor;
#
#     Tiles.stairs = new TileType("stairs", true, true,
#         [lightGray(CharCode.identicalTo), darkGray(CharCode.identicalTo)]);
#
#     Tiles.grass = new TileType("grass", true, true,
#         [lightGreen('.'), green('.')]);
#
#     Tiles.tree = new TileType("tree", false, false, [
#       green(CharCode.blackUpPointingTriangle, Color.darkGreen),
#       darkGreen(CharCode.blackUpPointingTriangle)
#     ]);
#
#     Tiles.treeAlt1 = new TileType("tree", false, false, [
#       green(CharCode.blackSpadeSuit, Color.darkGreen),
#       darkGreen(CharCode.blackSpadeSuit)
#     ]);
#
#     Tiles.treeAlt2 = new TileType("tree", false, false, [
#       green(CharCode.blackClubSuit, Color.darkGreen),
#       darkGreen(CharCode.blackClubSuit)
#     ]);
#   }
# }
# inflate method should shrink rect tangle
        # Rect inflate(double delta) {
        #   return Rect.fromLTRB(left - delta, top - delta, right + delta, bottom + delta);
        #    }
# def inflate(left, top, right, bottom):
#     return (left )





