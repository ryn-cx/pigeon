# TODO: Validate
import pytest
from get_around import build_client_automatically

from pigeon import Pigeon


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Pigeon:
    return Pigeon(build_client_automatically())
