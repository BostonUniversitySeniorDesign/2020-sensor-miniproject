import subprocess
import pytest
import sys


@pytest.fixture()
def servlet():
    with subprocess.Popen([sys.executable, "-m", "sp_iotsim.server"]) as proc:
        yield proc
