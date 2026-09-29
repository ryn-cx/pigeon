# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pigeon.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from pigeon import Pigeon

MOVIE_IDS = [
    pytest.param("b6303073-41bf-3644-8e71-0e8278c33678", id="movie"),
]

NOT_MOVIE_IDS = [
    pytest.param(
        "00000000-0000-0000-0000-000000000000",
        id="movie that does not exist",
    ),
    pytest.param("4902514835143843112", id="show asked for as a movie"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: Pigeon, movie_id: str) -> None:
    movie = client.movie(movie_id)
    assert str(movie.attributes.provider_variant_id) == movie_id


# TODO: Validate
@pytest.mark.parametrize("movie_id", NOT_MOVIE_IDS)
def test_download_invalid(client: Pigeon, movie_id: str) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.download(movie_id)
