from typing import TypeVar, Generic, Union

import httpx
from httpx import Response, Request, Timeout, URL

from ._constants import DEFAULT_TIMEOUT


HttpxClientT = TypeVar("HttpxClientT", bound=[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[HttpxClientT]):
    _client: HttpxClientT

    _base_url = URL("https://api.opendota.com/api/")
    _timeout = DEFAULT_TIMEOUT

    def _prepare_url(self, url: Union[str, URL]) -> URL:
        merge_url = URL(url)
        if merge_url.is_relative_url:
            merge_raw_path = self.base_url.raw_path + merge_url.raw_path.lstrip(b"/")
            return self.base_url.copy_with(raw_path=merge_raw_path)

    def _build_request(self, method: str, url: str, **kwargs) -> Request:
        return self._client.build_request(
            method=method, url=self._prepare_url(url), **kwargs)

    @property
    def base_url(self) -> URL:
        return self._base_url

    @base_url.setter
    def base_url(self, url: Union[str, URL]) -> None:
        self._base_url = URL(base_url) if isinstance(base_url, str) else base_url


class SyncAPIClient(BaseClient[httpx.Client]):
    _client: httpx.Client

    def __init__(self, *, timeout: Union[float, Timeout, None] = None) -> None:
        if not timeout:
            timeout = self._timeout

        self._client = httpx.Client(timeout=timeout, base_url=self.base_url)

    def close(self) -> None:
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self) -> "SyncAPIClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def request(self, method: str, url: str, **kwargs) -> Response:
        return self._client.send(self._build_request(method, url, **kwargs))

    def get(self, url: str, **kwargs) -> Response:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> Response:
        return self.request("POST", url, **kwargs)

