# https://websockets.readthedocs.io/en/stable/reference/index.html

import asyncio
from websockets.server import serve
messages = []

async def echo(websocket):
    offset = 0
    async for message in websocket:
        print(message)
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())