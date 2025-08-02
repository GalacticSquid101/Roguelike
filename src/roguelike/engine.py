"""Module defining the game engine"""
from typing import Set, Iterable, Any

from auto_all import start_all, end_all # type: ignore[import-untyped]
from tcod.context import Context
from tcod.console import Console

from .entity import Entity
from .game_map import GameMap
from .input_handlers import EventHandler

start_all()

class Engine:
    """The game engine itself"""
    def __init__(self,
                 entities: Set[Entity],
                 event_handler: EventHandler,
                 game_map: GameMap,
                 player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        """The game engine event handler"""
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """render all entities to the screen"""
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()

end_all()
