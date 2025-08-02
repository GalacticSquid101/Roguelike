"""Module containing procedural generation"""
import random
from typing import Iterator

from auto_all import start_all, end_all # type: ignore[import-untyped]

from .game_map import GameMap
from .tile_types import wall, floor

start_all()

class RectangularRoom:
    """Class defining a rectangular room"""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> tuple[int, int]:
        """Returns the center point of the room"""
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index"""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
    
def tunnel_between(
        start: tuple[int, int], end: tuple[int, int]
) -> Iterator[tuple[int, int]]:
    """Return an L-shaped tunnel between these two points"""
    

def generate_dungeon(map_width: int, map_height: int) -> GameMap:
    """Function to generate a game map and populate it randomly"""
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = floor
    dungeon.tiles[room_2.inner] = floor

    return dungeon

end_all()
