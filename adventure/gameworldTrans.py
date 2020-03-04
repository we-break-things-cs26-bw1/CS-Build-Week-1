#pos are x Tuple
#stage is the global playare
class Stage():
    def __init__(self,tiles,width,height,bounds,items,_numExplorable,_visibilityDirty = True,):
        """
        :type bounds: Rect (0,0), (9,9)
        :type tiles: 2darray
        :type items: list(Items)
        :type _numExplorabl: int
        """
        self.tiles=[[0 for j in range(height)] for i in range(width)]
        self.width=width
        self.height=height
        self.bounds=bounds
        self.tiles=tiles
        self.items=items
        self._visibilityDirty = _visibilityDirty
        self._numExplorable=_numExplorable
    def __getitem__(self, pos):
        """"
        :type pos:Vector (0,0)
        """
        if pos in self.tiles:
            return self.tiles[pos]
        #tiles as mapp
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
        #inflate method should shrink rect tangle
        #Rect inflate(double delta) {
        #   return Rect.fromLTRB(left - delta, top - delta, right + delta, bottom + delta);
        #    }
        for pos in self.bounds.inflate(-1):
            tile =self[pos]
            of
class Tile():
    def __init__(self,pos,type):
        self.pos= pos
        self.type=type
class StageBuilder():
    def __init__(self,stage:Stage):
        self.stage=stage
    def getTile(self,pos):
        self.stage
    def setTile(self,pos,tile):
        selfstage.
class dungeon (StageBuilder)
    def __init__(self,numRoomTries,extraConnectorChance,roomExtraSize,windingPercent,_rooms,_regions,_currrentRegion=1):
        self.numRoomTries = numRoomTries
        #positive int
        self.extraConnectorChance= extraConnectorChance
        #percentage i.e 20/100
        self.roomExtraSize =roomExtraSize
        ##allows rooms to be larger, int
        self.windingPercent=windingPercent
        #int/100
        self._rooms=_rooms
        #<rect>[]
        self.regions=_regions
        #for each open position in the dungeon, the index of the connected region that that position is part of
        self.currentRegion=_currrentRegion
    def generate(self,stage:Stage):
        if stage.width % 2==0 or stage.height%2 ==0:
            raise ValueError ("the stage be odd-sized")
    def setTile(self, TileType):




