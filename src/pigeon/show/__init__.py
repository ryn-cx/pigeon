# TODO: Validate
"""Contains the Show class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from pigeon.base_api_endpoint import BaseEndpoint
from pigeon.exceptions import ResourceNotFoundError, ShowNotFoundError
from pigeon.show.models import ShowModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

SHOW_TYPE = "CATALOGUE/SERIES"

REPRESENT = (
    "(items(items),recs[take=8],collections(items(items[take=8])),trailers,campaigns)"
)
"""Every season with its episodes, the recommendations, extras and trailers."""


# TODO: Validate
class Show(BaseEndpoint):
    """Contains the show.

    A show is looked up by the series id at the end of its watch page, e.g.
    4902514835143843112 in https://www.peacocktv.com/watch/asset/tv/the-office/4902514835143843112.

    Source: https://atom.peacocktv.com/adapter-calypso/v3/query/node/provider_series_id/{series_id}

    Example request:
        - GET /adapter-calypso/v3/query/node/provider_series_id/{series_id} HTTP/2
        - Host: atom.peacocktv.com
        - Accept: application/json
        - X-SkyOTT-Proposition: NBCUOTT
        - X-SkyOTT-Provider: NBCU
        - X-SkyOTT-Language: en
        - X-SkyOTT-Platform: PC
        - X-SkyOTT-Territory: US
        - X-SkyOTT-Device: COMPUTER
    """

    # TODO: Validate
    def __call__(self, series_id: str) -> ShowModel:
        """Download and parse the show file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: str) -> str:
        """Download the show file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"provider_series_id/{series_id}",
                params={"represent": REPRESENT},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(series_id, err.status_code, err.response) from err
        return self._validate_download(response, series_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, series_id: str) -> str:
        show = json.loads(response)
        if (
            show.get("type") != SHOW_TYPE
            or show.get("attributes", {}).get("providerSeriesId") != series_id
            or "items" not in show.get("relationships", {})
        ):
            raise ShowNotFoundError(series_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ShowModel:
        """Load a show file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
