from .._router import SyncAPIRouter


class Hero(SyncAPIRouter):
    router_path = "heroes"

    def __call__(self, hero_id: int):
        return self._get(hero_id, "matches").json()

    def get_heroes(self):
        return self._get().json()

    def get_matchups(self, hero_id: int):
        return self._get(hero_id, "matchups").json()

    def get_durations(self, hero_id: int):
        return self._get(hero_id, "durations").json()

    def get_players(self, hero_id: int):
        return self._get(hero_id, "players").json()

    def get_item_popularity(self, hero_id: int):
        return self._get(hero_id, "itemPopularity").json()

    def get_stats(self):
        return self._get(router_path="heroStats").json()

    def get_benchmarks(self, hero_id: int):
        return self._get(router_path="benchmarks", params={"hero_id": hero_id}).json()
