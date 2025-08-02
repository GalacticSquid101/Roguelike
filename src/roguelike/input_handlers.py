"""The input handlers for different controls"""
from typing import override

from auto_all import start_all, end_all # type: ignore[import-untyped]
import tcod.event
import tcod.event_constants

from .actions import Action, EscapeAction, MovementAction

start_all()

class EventHandler(tcod.event.EventDispatch[Action]):
    """The event handler to handle events from the user"""

    @override
    def ev_quit(self, event: tcod.event.Quit) -> Action | None:
        """Method for when the quit event happens"""
        raise SystemExit()

    @override
    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        """Method for keydown events"""
        action: Action | None = None

        key = event.sym

        match key:
            case tcod.event_constants.K_UP:
                action = MovementAction(dx=0, dy=-1)
            case tcod.event_constants.K_DOWN:
                action = MovementAction(dx=0, dy=1)
            case tcod.event_constants.K_LEFT:
                action = MovementAction(dx=-1, dy=0)
            case tcod.event_constants.K_RIGHT:
                action = MovementAction(dx=1, dy=0)
            case tcod.event_constants.K_ESCAPE:
                action = EscapeAction()

        return action

end_all()
