# TODO: Validate
from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import generate_all

import generate
from pigeon import Pigeon

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all(generate, Pigeon(build_client_automatically()))
