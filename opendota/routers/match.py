from typing import List, Union

from .._router import SyncAPIRouter


class Match(SyncAPIRouter):
    router_path = "matches"

    def __call__(self, match_id: int):
        return self._get(match_id).json()

    def get_pro_matches(self):
        return self._get(router_path="proMatches").json()

    def get_public_matches(self):
        return self._get(router_path="publicMatches").json()

    def get_parsed_matches(self):
        return self._get(router_path="parsedMatches").json()

    def find_matches(
        self,
        *,
        team_a: Union[List[int], None] = None,
        team_b: Union[List[int], None] = None,
    ):
        return self._get(
            router_path="findMatches",
            params=self._prepare_params({"teamA": team_a, "teamB": team_b}),
        ).json()
