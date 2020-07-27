import sp_iotsim as s


def test_ini():
    rooms = s.get_simulated_rooms()
    assert isinstance(rooms, dict)

    assert sorted(rooms["lab1"].keys()) == ["co", "loc", "occ", "scale"], "wrong keys"
