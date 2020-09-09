"""
WebSockets server

This program generates simulated data for multiple rooms, with multiple sensors per room.

The default behavior is to be only visible on the computer itself by parameter "localhost"
so that no firewall edits are needed.

The port number is arbitrary, as long as the server and client are on the same port all is well.

Naturally, this server must be started before the client(s) attempt to connect.
"""

from scipy.stats import erlang, cauchy, poisson, gamma
import random
import json
import asyncio
import typing as T
import configparser
from datetime import datetime
import importlib.resources
import websockets
import argparse

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


def generate_data(room: T.Dict[str, float]) -> T.Dict[str, T.Union[str, float]]:
    """
    generate simulated data
    """

    return {
        "time": datetime.now().isoformat(),
        "temperature": cauchy.rvs(loc=room["loc"], scale=room["scale"], size=1).tolist(),
        "occupancy": poisson.rvs(room["occ"], size=1).tolist(),
        "co2": gamma.rvs(room["co"], size=1).tolist(),
    }


async def iot_handler(websocket, path):
    """
    generate simulated data for each room and sensor
    """

    await websocket.send(motd)

    rooms = get_simulated_rooms()

    print("Connected:", websocket.remote_address)
    while True:
        await asyncio.sleep(erlang.rvs(1, 0, size=1).item())

        room = random.choice(list(rooms.keys()))

        try:
            await websocket.send(json.dumps({room: generate_data(rooms[room])}))
        except websockets.exceptions.ConnectionClosedOK:
            break

    print("Closed:", websocket.remote_address)


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


def cli():
    p = argparse.ArgumentParser(description="WebSocket IoT simulator server")
    p.add_argument("host", help="Host address", nargs="?", default="localhost")
    p.add_argument("port", help="network port", nargs="?", type=int, default=8765)
    P = p.parse_args()

    print("IoT server starting: ", P.host, "port", P.port)
    asyncio.run(main(P.host, P.port))


if __name__ == "__main__":
    cli()
