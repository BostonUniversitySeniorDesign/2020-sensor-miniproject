import sp_iotsim.server as server


def test_ini():
    rooms = server.get_simulated_rooms()
    assert isinstance(rooms, dict)

    assert sorted(rooms["lab1"].keys()) == ["co", "loc", "occ", "scale"], "wrong keys"
