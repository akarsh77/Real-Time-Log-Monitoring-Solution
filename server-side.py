import asyncio
import websockets
import os

LOG_FILE = 'logFile.log'

async def echo(websocket, path):
    with open(LOG_FILE, 'r') as fp:
        Lines = fp.readlines() [-10:] # read 10 lines
        for line in Lines:
            await websocket.send(line.strip())
        fp.seek(0, 2)
        while True:
            line = fp.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
            await websocket.send(line.strip())

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
