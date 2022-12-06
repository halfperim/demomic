from tuning import Tuning
import usb.core
import usb.util
import time
import asyncio
import json
import websockets

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

async def handler(websocket):
    if dev:
        Mic_tuning = Tuning(dev)
        while True:
            try:
                print(Mic_tuning.direction)
                result = {"angle": Mic_tuning.direction}
                await websocket.send(json.dumps(result))
                # print("data sent")
                confirmation = await websocket.recv()
                print(confirmation)
                time.sleep(1)
            except KeyboardInterrupt:
                break



# async def handler(websocket):
#     while True:
#         try:
#             message = await websocket.recv()
#         except websockets.ConnectionClosedOK:
#             break
#         print(message)

async def main():
    async with websockets.serve(handler,"10.48.45.131",8001):
        await asyncio.Future()

if __name__=="__main__":
    asyncio.run(main())


# dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

# if dev:
#     Mic_tuning = Tuning(dev)
#     print(Mic_tuning.direction)
#     while True:
#         try:
#             print(Mic_tuning.direction)
#             time.sleep(1)
#         except KeyboardInterrupt:
#             break

# devices = usb.core.find(find_all=True)
# print(devices)

