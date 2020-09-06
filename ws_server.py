#!/usr/bin/env python3
"""
WebSockets server

This program generates simulated data for multiple rooms, with multiple sensors per room.

The default behavior is to be only visible on the computer itself by parameter "localhost"
so that no firewall edits are needed.

The port number is arbitrary, as long as the server and client are on the same port all is well.

Naturally, this server must be started before the client(s) attempt to connect.
"""

import argparse
import asyncio

from sp_iotsim.server import main


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="WebSocket IoT simulator server")
    p.add_argument("host", help="Host address", nargs="?", default="localhost")
    p.add_argument("port", help="network port", nargs="?", type=int, default=8765)
    P = p.parse_args()

    asyncio.run(main(P.host, P.port))
