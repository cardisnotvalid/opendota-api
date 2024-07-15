from .._router import SyncAPIRouter


class League(SyncAPIRouter):
    router_path = "leagues"

    def __call__(self, league_id: int):
        return self._get(league_id).json()

    def get_leagues(self):
        return self._get().json()

    def get_matches(self, league_id: int):
        return self._get(league_id, "matches").json()

    def get_teams(self, league_id: int):
        return self._get(league_id, "teams").json()
