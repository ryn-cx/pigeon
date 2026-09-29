# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class PigeonError(Exception):
    """Base exception for Pigeon."""

    response: str | dict[str, Any] | None = None
    """The data that caused the error, or None if there was none."""


# TODO: Validate
class HTTPError(PigeonError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested node does not exist."""


# TODO: Validate
class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id and the originating response."""
        self.series_id = series_id
        super().__init__(status_code, response)


# TODO: Validate
class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    # TODO: Validate
    def __init__(
        self,
        movie_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.movie_id = movie_id
        super().__init__(status_code, response)


# TODO: Validate
class CollectionNotFoundError(ResourceNotFoundError):
    """Raised when the requested collection does not exist."""

    # TODO: Validate
    def __init__(
        self,
        slug: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the collection slug and the originating response."""
        self.slug = slug
        super().__init__(status_code, response)
