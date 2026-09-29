# TODO: Validate
"""Contains the Movie class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from pigeon.base_api_endpoint import BaseEndpoint
from pigeon.exceptions import MovieNotFoundError, ResourceNotFoundError
from pigeon.movie.models import MovieModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

MOVIE_TYPE = "ASSET/PROGRAMME"

REPRESENT = "(recs[take=8],collections(items(items[take=8])),trailers,campaigns)"
"""The recommendations, extras and trailers."""


# TODO: Validate
class Movie(BaseEndpoint):
    """Contains the movie.

    A movie is looked up by the id at the end of its watch page, e.g.
    b6303073-41bf-3644-8e71-0e8278c33678 in https://www.peacocktv.com/watch/asset/movies/shrek/b6303073-41bf-3644-8e71-0e8278c33678.

    Source: https://atom.peacocktv.com/adapter-calypso/v3/query/node/provider_variant_id/{movie_id}

    Example request:
        - GET /adapter-calypso/v3/query/node/provider_variant_id/{movie_id} HTTP/2
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
    def __call__(self, movie_id: str) -> MovieModel:
        """Download and parse the movie file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: str) -> str:
        """Download the movie file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"provider_variant_id/{movie_id}",
                params={"represent": REPRESENT},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
        return self._validate_download(response, movie_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, movie_id: str) -> str:
        movie = json.loads(response)
        if (
            movie.get("type") != MOVIE_TYPE
            or movie.get("attributes", {}).get("providerVariantId") != movie_id
        ):
            raise MovieNotFoundError(movie_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MovieModel:
        """Load a movie file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
