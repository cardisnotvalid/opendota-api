from .._router import SyncAPIRouter


class Player(SyncAPIRouter):
    router_path = "players"

    def __call__(self, account_id: int):
        return self._get(account_id).json()

    def get_wl(self, account_id: int):
        return self._get(account_id, "wl").json()

    def get_matches(self, account_id: int):
        return self._get(account_id, "matches").json()

    def get_recent_matches(self, account_id: int):
        return self._get(account_id, "recentMatches").json()

    def get_heroes(self, account_id: int):
        return self._get(account_id, "heroes").json()

    def get_peers(self, account_id: int):
        return self._get(account_id, "peers").json()

    def get_pros(self, account_id: int):
        return self._get(account_id, "pros").json()

    def get_totals(self, account_id: int):
        return self._get(account_id, "totals").json()

    def get_counts(self, account_id: int):
        return self._get(account_id, "counts").json()

    def get_histograms(self, account_id: int):
        return self._get(account_id, "histograms").json()

    def get_ward_map(self, account_id: int):
        return self._get(account_id, "wardmap").json()

    def get_word_cloud(self, account_id: int):
        return self._get(account_id, "wordcloud").json()

    def get_ratings(self, account_id: int):
        return self._get(account_id, "ratings").json()

    def get_rankings(self, account_id: int):
        return self._get(account_id, "rankings").json()

    def refresh(self, account_id: int):
        return self._post(account_id, "refresh")

    def search(self, query: str):
        return self._get(router_path="search", params={"q": query}).json()

    def get_top_players(self):
        return self._get(router_path="rankings").json()
