# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pigeon.exceptions import CollectionNotFoundError

if TYPE_CHECKING:
    from pigeon import Pigeon

PAGE_SIZE = 5


# TODO: Validate
def test_download_page(client: Pigeon) -> None:
    collection = client.collection("/movies/a-z", skip=10, take=PAGE_SIZE)
    assert collection.attributes.slug == "/movies/a-z"
    assert len(collection.relationships.items.data) == PAGE_SIZE


# TODO: Validate
def test_download_all(client: Pigeon) -> None:
    collection = client.collection("/tv/iceberg-tv-popular-on-peacock")
    assert collection.relationships.items.data


# TODO: Validate
def test_download_invalid(client: Pigeon) -> None:
    with pytest.raises(CollectionNotFoundError):
        client.collection.download("/not/a-collection")
