from .._router import SyncAPIRouter


class Match(SyncAPIRouter):
    router_path = "matches"

    def get_match(self, match_id: int):
        return self._get(match_id).json()
