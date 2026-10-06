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

MODEL_NAME = "ShowModel"


# TODO: Validate
class ShowId(RecordingId[Pigeon]):
    series_id: str

    # TODO: Validate
    def download(self, client: Pigeon) -> str:
        return client.show.download(self.series_id)


SHOWS = load_ids(GENERATOR_PATHS, MODEL_NAME, ShowId)


# TODO: Validate
def generate_show(client: Pigeon) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SHOWS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ShowId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(Pigeon(build_client_automatically()))
