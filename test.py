import asyncio
import psutil
import socketserver
import sys
import multiprocessing
import time

import redis
import redis.asyncio


class PotatoServer(socketserver.ThreadingTCPServer):
    def get_request(self):
        return self.socket.accept()


class PotatoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        time.sleep(60)
        "bye"


def redis_mock_sync():
    with PotatoServer(("localhost", 6379), PotatoHandler) as server:
        server.serve_forever()


def redis_kwargs():
    return dict(
        host="localhost",
        port=6379,
        client_name="Hi Andy!",
        health_check_interval=10,
        retry_on_timeout=True,
        socket_timeout=0.01,
    )


def main_sync():
    t = multiprocessing.Process(target=redis_mock_sync, daemon=True)
    t.start()
    psutil.Process().nice(1)
    try:
        r = redis.Redis(connection_pool=redis.BlockingConnectionPool(**redis_kwargs()))
        print(r.ping())
    finally:
        t.terminate()

async def main():
    t = multiprocessing.Process(target=redis_mock_sync, daemon=True)
    t.start()
    psutil.Process().nice(1)
    try:
        r = redis.asyncio.Redis(connection_pool=redis.asyncio.BlockingConnectionPool(**redis_kwargs()))
        await r.ping()
    finally:
        t.terminate()


if __name__ == "__main__":
    if sys.argv[1:2] == ["sync"]:
        main_sync()
    else:
        asyncio.run(main())
