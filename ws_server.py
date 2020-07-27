#!/usr/bin/env python3
"""
WebSockets server
"""

import argparse
import asyncio
import websockets
from sp_iotsim import iot_handler

PORT = 8765

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="WebSocket server")
    p.add_argument("host", help="Host address", nargs="?", default="localhost")
    p.add_argument("port", help="network port", nargs="?", type=int, default=8765)
    P = p.parse_args()

    print("SERVER: port", PORT)
    start_server = websockets.serve(
        iot_handler,
        host="localhost",
        port=PORT,
        compression=None,
        max_size=2 ** 12,
        read_limit=2 ** 10,
        max_queue=4,
    )

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
