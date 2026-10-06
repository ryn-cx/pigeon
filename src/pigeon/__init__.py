# TODO: Validate
"""Contains the Pigeon class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import Any

from get_around import GetAround

from pigeon.collection import Collection
from pigeon.exceptions import HTTPError, ResourceNotFoundError
from pigeon.movie import Movie
from pigeon.show import Show

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_URL = "https://atom.peacocktv.com/adapter-calypso/v3/query/node"

CONTENT_SEGMENTS = "APPLETV,D2C,ESSENTIALS,Free,STARZ"


# TODO: Validate
class Pigeon:
    """Peacock API wrapper.

    Talks to the Atom API peacocktv.com reads its catalogue from. It needs no
    account.
    """

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        sleep_time: float = 0,
    ) -> None:
        """Initializes the Pigeon client.

        The client holds one attribute per endpoint, so `client.show(id)` looks
        a show up and `client.show.download(id)` and `client.show.load(data)`
        are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.sleep_time = sleep_time

        self.collection = Collection(self)
        self.movie = Movie(self)
        self.show = Show(self)

    # TODO: Validate
    def _headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "X-SkyOTT-Proposition": "NBCUOTT",
            "X-SkyOTT-Provider": "NBCU",
            "X-SkyOTT-Language": "en",
            "X-SkyOTT-Platform": "PC",
            "X-SkyOTT-Territory": "US",
            "X-SkyOTT-Device": "COMPUTER",
        }

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        log_id: str,
    ) -> str:
        """Download a node from the Atom API and return the body as text.

        Args:
            endpoint: The path under the node query to download, empty for a
                lookup by slug.
            params: The query parameters to send. A parameter set to None is
                left out.
            log_id: What the request is called in the log.

        Raises:
            ResourceNotFoundError: If nothing is under what was asked for.
            HTTPError: If the request is answered with any other error status.
        """
        logger.debug("Downloading: %s", log_id)
        url = f"{API_URL}/{endpoint}" if endpoint else API_URL
        start = monotonic()
        response = self.get_around_client.get(
            url,
            params={
                "features": "upcoming",
                "contentSegments": CONTENT_SEGMENTS,
                **{key: value for key, value in params.items() if value is not None},
            },
            headers=self._headers(),
            timeout=60,
        )

        if response.status_code != HTTPStatus.OK:
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text
