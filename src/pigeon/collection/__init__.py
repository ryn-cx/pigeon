# TODO: Validate
"""Contains the Collection class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from pigeon.base_api_endpoint import BaseEndpoint
from pigeon.collection.models import CollectionModel, model_validate_json
from pigeon.exceptions import CollectionNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

COLLECTION_TYPE = "CATALOGUE/COLLECTION"


# TODO: Validate
class Collection(BaseEndpoint):
    """Contains a collection of titles.

    A collection is looked up by its slug. These are the lists behind pages like
    https://www.peacocktv.com/stream/movies/a-z (`/movies/a-z`) and rails like
    Popular on Peacock (`/tv/iceberg-tv-popular-on-peacock`). `skip` and `take`
    page through the titles; left out, every title is returned.

    Source: https://atom.peacocktv.com/adapter-calypso/v3/query/node?slug={slug}

    Example request:
        - GET /adapter-calypso/v3/query/node?slug={slug}&represent=(items) HTTP/2
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
    def __call__(
        self,
        slug: str,
        skip: int | None = None,
        take: int | None = None,
    ) -> CollectionModel:
        """Download and parse the collection file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(slug, skip, take), log_id)

    # TODO: Validate
    def download(
        self,
        slug: str,
        skip: int | None = None,
        take: int | None = None,
    ) -> str:
        """Download the collection file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint="",
                params={"slug": slug, "represent": self._represent(skip, take)},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise CollectionNotFoundError(slug, err.status_code, err.response) from err
        return self._validate_download(response, slug)

    # TODO: Validate
    @staticmethod
    def _represent(skip: int | None, take: int | None) -> str:
        paging = [
            f"{name}={value}"
            for name, value in (("skip", skip), ("take", take))
            if value is not None
        ]
        if not paging:
            return "(items)"
        return f"(items[{','.join(paging)}])"

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, slug: str) -> str:
        collection = json.loads(response)
        if (
            collection.get("type") != COLLECTION_TYPE
            or collection.get("attributes", {}).get("slug") != slug
        ):
            raise CollectionNotFoundError(slug, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CollectionModel:
        """Load a collection file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
