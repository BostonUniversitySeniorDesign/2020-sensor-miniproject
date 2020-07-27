#!/usr/bin/env python3
"""
WebSockets client
"""

from pathlib import Path
import argparse
import asyncio
import websockets
import zlib
import sys
import typing as T
import typing.io as Ti


async def client(port: int, addr: str, max_packets: int, log_file: Path):

    log_file = Path(log_file).expanduser()

    uri = f"ws://{addr}:{port}"

    async with websockets.connect(uri) as websocket:
        qb = await websocket.recv()
        if isinstance(qb, bytes):
            print(zlib.decompress(qb).decode("utf8"))
        else:
            print(qb)

        with open(log_file, mode="a") as f:
            for i in range(max_packets):
                data = await websocket.recv()
                _handle_packet(data, f)
                if i % 5 == 0:
                    f.flush()


def _handle_packet(data: T.Union[str, bytes], f: Ti.TextIO):
    if isinstance(data, str):
        print(data)
        f.write(data + "\n")
    else:
        print(
            "unexpected binary data: ", data.decode("utf8", errors="ignore"), file=sys.stderr,
        )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="WebSocket client")
    p.add_argument("log_file", help="file to log JSON data")
    p.add_argument("-host", help="Host address", default="localhost")
    p.add_argument("-port", help="network port", type=int, default=8765)
    p.add_argument(
        "-max_packets",
        help="shut down program after total packages received",
        type=int,
        default=100000,
    )
    P = p.parse_args()

    try:
        asyncio.run(client(P.port, P.host, P.max_packets, P.log_file))
    except KeyboardInterrupt:
        print(P.log_file)
