from scipy.stats import erlang, cauchy, poisson, gamma
import random
import json
import asyncio
import typing as T
import configparser
from datetime import datetime
import importlib.resources
import websockets

motd = b"x\x9csuvU\x08N\xcd\xcb\xcc/RpN,(.\xc9\xcfKU\xf0\xcc\x0fQ(\xce\xcc-\xcdI,\xc9/\x02\x00\xbe\xce\x0b\xe7"


def get_simulated_rooms() -> T.Dict[str, T.Dict[str, float]]:
    """
    retrieves simulated room names and parameters
    """

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
    """
    generate simulated data for each room and sensor
    """

    await websocket.send(motd)
    mode = "all"

    rooms = get_simulated_rooms()

    print("IoT simulator connected to", websocket.remote_address)
    while True:
        await asyncio.sleep(erlang.rvs(1, 0, size=1).item())

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

        try:
            await websocket.send(json.dumps({room: dat}))
        except websockets.exceptions.ConnectionClosedOK:
            print("Closing connection to", websocket.remote_address)
            break


async def main(host: str, port: int):
    """
    starts the server and closes client connections

    keeps running until user Ctrl-C
    """

    server = await websockets.serve(
        iot_handler,
        host=host,
        port=port,
        compression=None,
        max_size=2 ** 12,
        read_limit=2 ** 10,
        max_queue=4,
    )

    await server.wait_closed()
