import sp_iotsim.server as server
import sp_iotsim.client as client
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


@pytest.mark.timeout(20)
def test_server(servlet):
    asyncio.run(client.main(8765, "localhost", 5))
    servlet.terminate()
