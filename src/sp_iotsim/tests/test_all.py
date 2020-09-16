import sp_iotsim.server as server
import sp_iotsim.client as client
import sp_iotsim.fileio as fio
import random
import asyncio
import pytest


def test_ini():
    rooms = server.get_simulated_rooms()
    assert isinstance(rooms, dict)

    assert sorted(rooms["lab1"].keys()) == ["co", "loc", "occ", "scale"], "wrong keys"


def test_generate():
    rooms = server.get_simulated_rooms()
    room = random.choice(list(rooms.keys()))

    dat = server.generate_data(rooms[room])

    assert sorted(dat.keys()) == ["co2", "occupancy", "temperature", "time"], "wrong keys"


def test_need_logcode(servlet, tmp_path):

    with pytest.raises(NotImplementedError):
        asyncio.run(client.main(8765, "localhost", 2, log_file=tmp_path / "nobody.txt"))
    servlet.terminate()


def test_server_client(servlet, capsys, tmp_path):
    """
    this is not a typical way to write a data file, but is used here
    since the assignment tasks include writing a file so I did this test
    unconventionally
    """
    N = 2
    fn = tmp_path / "test.log"

    asyncio.run(client.main(8765, "localhost", N))
    servlet.terminate()

    stdout, stderr = capsys.readouterr()
    fn.write_text(stdout.split("\n", 1)[1])

    dat = fio.load_data(fn)
    assert sorted(dat.keys()) == ["co2", "occupancy", "temperature"], "wrong keys"
