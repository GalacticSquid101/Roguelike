"""A module to contain the Entity base class"""
from auto_all import start_all, end_all # type: ignore[import-untyped]

start_all()

class Entity:
    """A generic object to represent players, enemies, items, etc."""
    def __init__(self, x: int, y: int, char: str, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        """Move the entity the given amount"""
        self.x += dx
        self.y += dy

end_all()
