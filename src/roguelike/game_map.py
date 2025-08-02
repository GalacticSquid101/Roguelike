"""Module defines the game map"""

from auto_all import start_all, end_all # type: ignore[import-untyped]
import numpy as np
from tcod.console import Console

from .tile_types import floor, wall

start_all()

class GameMap:
    """The instance of the game map"""
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=wall, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """Returns True if x and y are inside of the bounds of this map"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console:Console) -> None:
        """Renders the game map"""
        console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]

end_all()
