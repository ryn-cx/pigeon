# TODO: Validate
from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from pigeon import Pigeon

MODEL_NAME = "MovieModel"


# TODO: Validate
class MovieId(RecordingId[Pigeon]):
    movie_id: str

    # TODO: Validate
    def download(self, client: Pigeon) -> str:
        return client.movie.download(self.movie_id)


MOVIES = load_ids(GENERATOR_PATHS, MODEL_NAME, MovieId)


# TODO: Validate
def generate_movie(client: Pigeon) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, MOVIES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MovieId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie(Pigeon(build_client_automatically()))
