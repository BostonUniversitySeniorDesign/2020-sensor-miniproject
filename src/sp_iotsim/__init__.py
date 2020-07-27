from scipy.stats import erlang, cauchy, poisson, gamma
import random
import json
import asyncio
import typing as T
import configparser
from datetime import datetime
import importlib.resources

motd = b"x\x9csuvU\x08N\xcd\xcb\xcc/RpN,(.\xc9\xcfKU\xf0\xcc\x0fQ(\xce\xcc-\xcdI,\xc9/\x02\x00\xbe\xce\x0b\xe7"


def get_simulated_rooms() -> T.Dict[str, T.Dict[str, float]]:
    C = configparser.ConfigParser()
    with importlib.resources.path(__package__, "config.ini") as f:
        ini = f.read_text()
    C.read_string(ini)

    rooms: T.Dict[str, T.Dict[str, float]] = {}
    for k in C.sections():
        rooms[k] = {}
        for j in C.options(k):
            rooms[k][j] = C.getfloat(k, j)

    return rooms


async def iot_handler(websocket, path):
    await websocket.send(motd)
    # mode_query = "What kind of sensor would you like? (temperature,occupancy)"
    # await websocket.send(mode_query)

    # mode = await websocket.recv()
    mode = "all"

    rooms = get_simulated_rooms()

    while True:
        await asyncio.sleep(erlang.rvs(1, 0, size=1))

        room = random.choice(list(rooms.keys()))
        dat = {"time": datetime.now().isoformat()}

        if mode.startswith(("all", "tem")):
            dat["temperature"] = cauchy.rvs(
                loc=rooms[room]["loc"], scale=rooms[room]["scale"], size=1
            ).tolist()
        if mode.startswith(("all", "occ")):
            dat["occupancy"] = poisson.rvs(rooms[room]["occ"], size=1).tolist()
        if mode.startswith(("all", "co")):
            dat["co2"] = gamma.rvs(rooms[room]["co"], size=1).tolist()

        await websocket.send(json.dumps({room: dat}))
