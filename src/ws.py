import websocket
import os
import _thread
import time
import rel
from dotenv import load_dotenv
load_dotenv()


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")


if __name__ == "__main__":
    uri = 'ws://' + os.getenv('USER') + ':8181/core'
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(uri,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    ws.run_forever(dispatcher=rel, reconnect=5)
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
