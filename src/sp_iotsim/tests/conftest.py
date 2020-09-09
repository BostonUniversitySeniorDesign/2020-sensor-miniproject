import subprocess
import pytest
import sys
import time


@pytest.fixture()
def servlet():
    with subprocess.Popen([sys.executable, "-m", "sp_iotsim.server"]) as proc:
        time.sleep(2)  # to avoid race with client
        yield proc
