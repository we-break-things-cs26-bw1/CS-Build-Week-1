# pos are x Tuple

# stage is the global playare

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

# heh stupid helper function
import random

from pygame.rect import Rect


class RNG():
    def vecInRect(self):
        pass

    def oneIn(self):
        random.randrange(self)


rng = RNG()


def twoTupleAdd(tuple1, tuplle2):
    return tuple1[0] + tuplle2[0], tuple1[1] + tuplle2[1]


def twoTupleMultiply(tuple1, multi):
    return tuple1[0] * multi, tuple1[1] * multi


def Array2d(width, height):
    return [[0] * width] * height


class Direction:
    none = (0, 0)
    n = (0, -1)
    ne = (1, -1)
    e = (1, 0)
    se = (1, 1)
    s = (0, 1)
    sw = (-1, 1)
    w = (-1, 0)
    nw = (-1, -1)

    all = [n, ne, e, se, s, sw, w, nw]

    cardinal = [n, e, s, w]

    intercardinal = [ne, se, sw, nw]


class Stage():
    def __init__(self, tiles, width, height, bounds, items, _numExplorable, _visibilityDirty=True, ):
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
        for pos in self.bounds.inflate(-1):
            tile: Tile = self[pos]
            if (tile.isTraversable):
                self._numExplorable += 1
            else:
                for dir in Direction.cardinal:
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
TileTypeMap[Floor]: TileType(name="floor", isPassable=True, isTraversable=True, appearance="gray")
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
            for dir in Direction.cardinal:
                tile = self.getTile(twoTupleAdd(pos, dir))
                if tile is floor: floors += 1
            #      // Prefer to erode tiles near more floor tiles so the erosion isn't too
            #     // spiky.
            if floors < 2: continue
            if rng.oneIn(9 - floors): self.setTile(pos, floor)


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
        self._currentRegion = _currrentRegion
        self.stage = stage

    def generate(self, stage: Stage):
        if stage.width % 2 == 0 or stage.height % 2 == 0:
            raise ValueError("the stage be odd-sized")
        self.bindStage(stage)
        self.fill(TileTypeMap[Wall])
        self._region = Array2d(stage.width, stage.height)
        self._addRooms()

        #  // Fill in all of the empty space with mazes.
        # state at 1, increment by 2 to the height of the bounds -w
        for y in range(1, self.stage.bounds.height, 2):
            for x in range(1, self.stage.bounds.width, 2):
                pos = (x, y)
                if self.getTile(pos) is not TileTypeMap[Wall]: continue
                self._growMaze(pos)

        self._connectRegions()
        self._removeDeadEnds()

        # self._rooms.forEach(onDecorateRoom)

    ##  /// Implementation of the "growing tree" algorithm from here:
    # /// http://www.astrolog.org/labyrnth/algrithm.htm.
    def _growMaze(self, start):
        cells = []  # ====list((0,0))
        self._startRegion()
        self._carve(start)
        cells.append(start)
        while not cells:
            cell = cells[-1]
            unmadeCells = []  # list of two tuples
            lastDir = None
            for dir in Direction.cardinal:
                if self._canCarve(cell, dir):
                    unmadeCells.add(dir)
            if unmadeCells:
                #         // Based on how "windy" passages are, try to prefer carving in the
                #         // same direction.
                dir = None
                # TODO() make sure this syntax is correct
                if unmadeCells.contains(lastDir) and rng.range(100) > self.windingPercent:
                    dir = lastDir
                else:
                    # TODO() implement random choice correctly
                    dir = rng.items(unmadeCells)

                self._carve(twoTupleAdd(cell, dir))
                self._carve(twoTupleMultiply(twoTupleAdd(cell, dir), 2))

                cells.append(twoTupleMultiply(twoTupleAdd(cell, dir), 2))
                lastDir = dir
            else:
                # TODO() fix synatax, may be like like remove[-1] or whatever
                cells.removeLast()
                # // This path has ended.
                # // No adjacent uncarved cells.
                lastDir = None

    #   /// Gets whether or not an opening can be carved from the given starting
    #   /// [Cell] at [pos] to the adjacent Cell facing [direction]. Returns `true`
    #   /// if the starting Cell is in bounds and the destination Cell is filled
    #   /// (or out of bounds).</returns>
    def _canCarve(self, pos, dir):
        if not self.bounds.contains(twoTupleMultiply(twoTupleAdd(pos + dir), 3)):
            return False
        else:
            return self.getTile(twoTupleMultiply(twoTupleAdd(pos + dir), 2)) == TileTypeMap[Wall]

    def _startRegion(self):
        self._currentRegion += 1

    #    // Find all of the tiles that can connect two (or more) regions.
    def _connectRegions(self):
        # // Find all of the tiles that can connect two (or more) regions.
        connectorRegions = {}  # two tuple (i.e. "vec") to set of unique ints
        for pos in self.bounds.inflate(-1):
            if self.getTile(pos) is not TileTypeMap[Wall]: continue
            regions = {}  # set of ints
            for dir in Direction.cardinal:
                checkForThis = twoTupleAdd(dir, pos)
                # TODO() check this out, make sure correct
                if checkForThis in self._regions.keys():
                    workingRegion = self._regions[checkForThis]
                    if workingRegion:
                        regions.add(workingRegion)
            if len(regions) < 2: continue
            connectorRegions[pos] = regions
        connectors = connectorRegions.keys()
        merged = {}
        openRegions = {}  # set of ints
        #     // Keep track of which regions have been merged. This maps an original
        #     // region index to the one it has been merged to.
        for i in range(self._currentRegion):
            merged[i] = i
            openRegions.add(i)

        #    // Keep connecting regions until we're down to one.
        while len(openRegions) > 1:
            # TODO() rng replacement
            connector = rng.item(connectors)
            #      // Carve the connection.
            self._addJunction(connector)

            # // Merge the connected regions. We'll pick one region (arbitrarily) and
            # // map all of the other regions to its index.

            regions = connectorRegions[connector]

            # TODO() MAKE SURE WE CAN MAP THE REGIONS TO THE MERGED REGION LIST
            # .map((region) = > merged[region]);

            dest = regions.first

            # find the answer from that sprint where you ordered dicts

            sources = list(regions)[1:]
            #
            #       // Merge all of the affected regions. We have to look at *all* of the
            #       // regions because other regions may have previously been merged with
            #       // some of the ones we're merging now.
            for i in range(self._currentRegion):
                if merged[i] in sources:
                    merged[i] = dest

            #        // The sources are no longer in use.
            openRegions.removeAll(sources)

            #       // Remove any connectors that aren't needed anymore
            #         // Don't allow connectors right next to each other.
            def removeWhere(pos):
                if connector - pos < 2: return True
                #   var regions = connectorRegions[pos].map((region) => merged[region])
                #             .toSet();
                regions = connectorRegions[pos].map(regions, merged[regions]).toSet()

                if len(regions) > 1: return False
                #        // This connecter isn't needed, but connect it occasionally so that the
                #     // dungeon isn't singly-connected.
                if rng.oneIn(self.extraConnectorChance): self._addJunction(pos)

                return True

    # may not be neccessary to impl
    # add addtional types if needed
    def _addJunction(self, pos):
        if rng.oneIn(4):
            self.setTile(pos, TileTypeMap[Floor])
        else:
            self.setTile(pos, TileTypeMap[Floor])

    def _removeDeadEnds(self):
        done = False
        while not done:
            done = True

            for pos in self.bounds.inflate(-1):
                if self.getTile(pos).type == TileTypeMap[Wall]: continue
                # // If it only has one exit, it's a dead end.
                exits = 0
                for dir in Direction.cardinal:
                    if self.getTile(twoTupleAdd(dir, pos)).type != TileTypeMap[Wall]: exits += 1

                if exits != 1: continue
                done = False
                self.setTile(pos, TileTypeMap[Wall])

    def _carve(self, pos, tileType):
        if tileType is None:
            tileType = TileTypeMap[Floor]
        self.setTile(pos, tileType)
        self._regions[pos] = self._currentRegion

    #   /// Places rooms ignoring the existing maze corridors.
    def _addRooms(self):
        pass

    def setTile(self, pos, type):
        self.stage[pos].type = type

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
#       green(CharCode.blackSpadeSuit, C# pos are x Tuple

# stage is the global playare

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

# heh stupid helper function
class RNG():
    def vecInRect(self):
        pass

    def oneIn(self):
        random


rng = RNG()


def twoTupleAdd(tuple1, tuplle2):
    return tuple1[0] + tuplle2[0], tuple1[1] + tuplle2[1]


def twoTupleMultiply(tuple1, multi):
    return tuple1[0] * multi, tuple1[1] * multi


def Array2d(width, height):
    return [[0] * width] * height


class Direction:
    none = (0, 0)
    n = (0, -1)
    ne = (1, -1)
    e = (1, 0)
    se = (1, 1)
    s = (0, 1)
    sw = (-1, 1)
    w = (-1, 0)
    nw = (-1, -1)

    all = [n, ne, e, se, s, sw, w, nw]

    cardinal = [n, e, s, w]

    intercardinal = [ne, se, sw, nw]


class Stage():
    def __init__(self, tiles, width, height, bounds, items, _numExplorable, _visibilityDirty=True, ):
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
        for pos in self.bounds.inflate(-1):
            tile: Tile = self[pos]
            if (tile.isTraversable):
                self._numExplorable += 1
            else:
                for dir in Direction.cardinal:
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
TileTypeMap[Floor]: TileType(name="floor", isPassable=True, isTraversable=True, appearance="gray")
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
            for dir in Direction.cardinal:
                tile = self.getTile(twoTupleAdd(pos, dir))
                if tile is floor: floors += 1
            #      // Prefer to erode tiles near more floor tiles so the erosion isn't too
            #     // spiky.
            if floors < 2: continue
            if rng.oneIn(9 - floors): self.setTile(pos, floor)


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
        self._currentRegion = _currrentRegion
        self.stage = stage

    def generate(self, stage: Stage):
        if stage.width % 2 == 0 or stage.height % 2 == 0:
            raise ValueError("the stage be odd-sized")
        self.bindStage(stage)
        self.fill(TileTypeMap[Wall])
        self._region = Array2d(stage.width, stage.height)
        self._addRooms()

        #  // Fill in all of the empty space with mazes.
        # state at 1, increment by 2 to the height of the bounds -w
        for y in range(1, self.stage.bounds.height, 2):
            for x in range(1, self.stage.bounds.width, 2):
                pos = (x, y)
                if self.getTile(pos) is not TileTypeMap[Wall]: continue
                self._growMaze(pos)

        self._connectRegions()
        self._removeDeadEnds()

        # self._rooms.forEach(onDecorateRoom)

    ##  /// Implementation of the "growing tree" algorithm from here:
    # /// http://www.astrolog.org/labyrnth/algrithm.htm.
    def _growMaze(self, start):
        cells = []  # ====list((0,0))
        self._startRegion()
        self._carve(start)
        cells.append(start)
        while not cells:
            cell = cells[-1]
            unmadeCells = []  # list of two tuples
            lastDir = None
            for dir in Direction.cardinal:
                if self._canCarve(cell, dir):
                    unmadeCells.add(dir)
            if unmadeCells:
                #         // Based on how "windy" passages are, try to prefer carving in the
                #         // same direction.
                dir = None
                # TODO() make sure this syntax is correct
                if unmadeCells.contains(lastDir) and rng.range(100) > self.windingPercent:
                    dir = lastDir
                else:
                    # TODO() implement random choice correctly
                    dir = rng.items(unmadeCells)

                self._carve(twoTupleAdd(cell, dir))
                self._carve(twoTupleMultiply(twoTupleAdd(cell, dir), 2))

                cells.append(twoTupleMultiply(twoTupleAdd(cell, dir), 2))
                lastDir = dir
            else:
                # TODO() fix synatax, may be like like remove[-1] or whatever
                cells.removeLast()
                # // This path has ended.
                # // No adjacent uncarved cells.
                lastDir = None

    #   /// Gets whether or not an opening can be carved from the given starting
    #   /// [Cell] at [pos] to the adjacent Cell facing [direction]. Returns `true`
    #   /// if the starting Cell is in bounds and the destination Cell is filled
    #   /// (or out of bounds).</returns>
    def _canCarve(self, pos, dir):
        if not self.bounds.contains(twoTupleMultiply(twoTupleAdd(pos + dir), 3)):
            return False
        else:
            return self.getTile(twoTupleMultiply(twoTupleAdd(pos + dir), 2)) == TileTypeMap[Wall]

    def _startRegion(self):
        self._currentRegion += 1

    #    // Find all of the tiles that can connect two (or more) regions.
    def _connectRegions(self):
        # // Find all of the tiles that can connect two (or more) regions.
        connectorRegions = {}  # two tuple (i.e. "vec") to set of unique ints
        for pos in self.bounds.inflate(-1):
            if self.getTile(pos) is not TileTypeMap[Wall]: continue
            regions = {}  # set of ints
            for dir in Direction.cardinal:
                checkForThis = twoTupleAdd(dir, pos)
                # TODO() check this out, make sure correct
                if checkForThis in self._regions.keys():
                    workingRegion = self._regions[checkForThis]
                    if workingRegion:
                        regions.add(workingRegion)
            if len(regions) < 2: continue
            connectorRegions[pos] = regions
        connectors = connectorRegions.keys()
        merged = {}
        openRegions = {}  # set of ints
        #     // Keep track of which regions have been merged. This maps an original
        #     // region index to the one it has been merged to.
        for i in range(self._currentRegion):
            merged[i] = i
            openRegions.add(i)

        #    // Keep connecting regions until we're down to one.
        while len(openRegions) > 1:
            # TODO() rng replacement
            connector = rng.item(connectors)
            #      // Carve the connection.
            self._addJunction(connector)

            # // Merge the connected regions. We'll pick one region (arbitrarily) and
            # // map all of the other regions to its index.

            regions = connectorRegions[connector]

            # TODO() MAKE SURE WE CAN MAP THE REGIONS TO THE MERGED REGION LIST
            # .map((region) = > merged[region]);

            dest = regions.first

            # find the answer from that sprint where you ordered dicts

            sources = list(regions)[1:]
            #
            #       // Merge all of the affected regions. We have to look at *all* of the
            #       // regions because other regions may have previously been merged with
            #       // some of the ones we're merging now.
            for i in range(self._currentRegion):
                if merged[i] in sources:
                    merged[i] = dest

            #        // The sources are no longer in use.
            openRegions.removeAll(sources)

            #       // Remove any connectors that aren't needed anymore
            #         // Don't allow connectors right next to each other.
            def removeWhere(pos):
                if connector - pos < 2: return True
                #   var regions = connectorRegions[pos].map((region) => merged[region])
                #             .toSet();
                regions = connectorRegions[pos].map(regions, merged[regions]).toSet()

                if len(regions) > 1: return False
                #        // This connecter isn't needed, but connect it occasionally so that the
                #     // dungeon isn't singly-connected.
                if rng.oneIn(self.extraConnectorChance): self._addJunction(pos)

                return True

    # may not be neccessary to impl
    # add addtional types if needed
    def _addJunction(self, pos):
        if rng.oneIn(4):
            self.setTile(pos, TileTypeMap[Floor])
        else:
            self.setTile(pos, TileTypeMap[Floor])

    def _removeDeadEnds(self):
        done = False
        while not done:
            done = True

            for pos in self.bounds.inflate(-1):
                if self.getTile(pos).type == TileTypeMap[Wall]: continue
                # // If it only has one exit, it's a dead end.
                exits = 0
                for dir in Direction.cardinal:
                    if self.getTile(twoTupleAdd(dir, pos)).type != TileTypeMap[Wall]: exits += 1

                if exits != 1: continue
                done = False
                self.setTile(pos, TileTypeMap[Wall])

    def _carve(self, pos, tileType):
        if tileType is None:
            tileType = TileTypeMap[Floor]
        self.setTile(pos, tileType)
        self._regions[pos] = self._currentRegion

    #   /// Places rooms ignoring the existing maze corridors.
    def _addRooms(self, numRoomTries=60):
        for i in range(0, numRoomTries):
            size = random.randrange(0, 1 + self.roomExtraSize) * 2 + 1 #Maybe need to truncate
            rectangularity = random.randrange(0, 1 + size / 2) * 2 + 1 #Maybe need to truncate
            width = size
            height = size
            if random.randint(1, 101) / 2 == 1:
                width += rectangularity
            else:
                height += rectangularity
                y = random.randrange((self.stage.bounds.height - height) / 2) * 2 + 1 # Maybe need to truncate
                x = random.randrange((self.stage.bounds.width - width) / 2) * 2 + 1 # Maybe need to truncate
                room = Rect(x, y, width, height)
                overlaps = False
                for i in self._rooms:
                    if room.distanceTo(other) <= 0:
                        overlaps = True
                        continue

            self._rooms += room

            self._startRegion()

            for pos in Rect(x, y, width, height):
                _carve(pos)





    def setTile(self, pos, type):
        self.stage[pos].type = type


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

#Tree growing algo






