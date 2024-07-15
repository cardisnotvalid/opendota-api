from . import routers
from ._base_client import SyncAPIClient


class OpenDota(SyncAPIClient):
    player: routers.Player
    match: routers.Match
    hero: routers.Hero

    def __init__(self) -> None:
        super().__init__()

        self.player = routers.Player(self)
        self.match = routers.Match(self)
        self.hero = routers.Hero(self)
