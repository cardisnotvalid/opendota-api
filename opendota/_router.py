from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from httpx import Response

if TYPE_CHECKING:
    from ._client import OpenDota


class SyncAPIRouter:
    _client: OpenDota

    router_path: str

    def __init__(self, client: OpenDota) -> None:
        self._client = client

    def _prepare_url(
        self,
        param: Union[int, str, None] = None,
        endpoint: Union[str, None] = None,
        *,
        router_path: Union[str, None] = None,
    ) -> str:
        if router_path:
            return router_path

        merge_url = f"{self.router_path}/{param}" if param else self.router_path
        return f"{merge_url}/{endpoint}" if endpoint else merge_url

    def _get(
        self,
        param: Union[str, int, None] = None,
        endpoint: Union[str, None] = None,
        *,
        params: Union[Dict[str, Any], None] = None,
        router_path: Union[str, None] = None,
    ) -> Response:
        return self._client.get(
            self._prepare_url(param, endpoint, router_path=router_path),
            params=params
        )

    def _post(
        self,
        param: Union[str, int, None] = None,
        endpoint: Union[str, None] = None,
        *,
        params: Union[Dict[str, Any], None] = None,
        router_path: Union[str, None] = None,
    ) -> Response:
        return self._client.post(
            self._prepare_url(param, endpoint, router_path=router_path),
            params=params
        )
