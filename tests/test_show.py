# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pigeon.exceptions import ShowNotFoundError

if TYPE_CHECKING:
    from pigeon import Pigeon

SHOW_IDS = [
    pytest.param("4902514835143843112", id="show with many seasons"),
    pytest.param("4873123615239886112", id="show with a single season"),
]

NOT_SHOW_IDS = [
    pytest.param("0000000000000000000", id="show that does not exist"),
    pytest.param(
        "b6303073-41bf-3644-8e71-0e8278c33678",
        id="movie asked for as a show",
    ),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SHOW_IDS)
def test_download(client: Pigeon, series_id: str) -> None:
    show = client.show(series_id)
    assert show.attributes.provider_series_id == series_id
    assert show.relationships.items.data


# TODO: Validate
@pytest.mark.parametrize("series_id", NOT_SHOW_IDS)
def test_download_invalid(client: Pigeon, series_id: str) -> None:
    with pytest.raises(ShowNotFoundError):
        client.show.download(series_id)
