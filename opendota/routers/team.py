from .._router import SyncAPIRouter


class Team(SyncAPIRouter):
    router_path = "teams"

    def __call__(self, team_id: int):
        return self._get(team_id).json()

    def get_teams(self):
        return self._get().json()

    def get_matches(self, team_id: int):
        return self._get(team_id, "matches").json()

    def get_players(self, team_id: int):
        return self._get(team_id, "players").json()

    def get_heroes(self, team_id: int):
        return self._get(team_id, "heroes").json()
