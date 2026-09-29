# TODO: Validate
from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from pigeon import Pigeon

MODEL_NAME = "CollectionModel"


# TODO: Validate
class CollectionId(RecordingId[Pigeon]):
    slug: str
    skip: int | None = None
    take: int | None = None

    # TODO: Validate
    def download(self, client: Pigeon) -> str:
        return client.collection.download(self.slug, self.skip, self.take)


COLLECTIONS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, CollectionId)


# TODO: Validate
def generate_collection(client: Pigeon) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, COLLECTIONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, CollectionId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_collection(Pigeon(build_client_automatically()))
