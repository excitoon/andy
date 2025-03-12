# Bug reproduction

## Useful commands

### Run

#### Async

```
docker compose run test
```

```
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 468, in send_packed_command
    await self.check_health()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 456, in check_health
    await self.retry.call_with_retry(self._send_ping, self._ping_failed)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/retry.py", line 59, in call_with_retry
    return await do()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 442, in _send_ping
    await self.send_command("PING", check_health=False)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 505, in send_command
    await self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 466, in send_packed_command
    await self.connect()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 296, in connect
    await self.on_connect()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 393, in on_connect
    await self.send_command("CLIENT", "SETNAME", self.client_name)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 505, in send_command
    await self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 468, in send_packed_command
    await self.check_health()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 456, in check_health
    await self.retry.call_with_retry(self._send_ping, self._ping_failed)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/retry.py", line 59, in call_with_retry
    return await do()
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 442, in _send_ping
    await self.send_command("PING", check_health=False)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 505, in send_command
    await self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 500, in send_packed_command
    await self.disconnect(nowait=True)
  File "/usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py", line 420, in disconnect
    async with async_timeout(self.socket_connect_timeout):
  File "/usr/local/lib/python3.10/site-packages/async_timeout/__init__.py", line 170, in __aenter__
    self._do_enter()
  File "/usr/local/lib/python3.10/site-packages/async_timeout/__init__.py", line 258, in _do_enter
    self._reschedule()
  File "/usr/local/lib/python3.10/site-packages/async_timeout/__init__.py", line 252, in _reschedule
    self._timeout_handler = self._loop.call_at(deadline, self._on_timeout)
  File "/usr/local/lib/python3.10/asyncio/base_events.py", line 736, in call_at
    timer = events.TimerHandle(when, callback, args, self, context)
  File "/usr/local/lib/python3.10/asyncio/events.py", line 105, in __init__
    super().__init__(callback, args, loop, context)
RecursionError: maximum recursion depth exceeded while calling a Python object
Task was destroyed but it is pending!
task: <Task pending name='Task-110' coro=<AbstractConnection._send_packed_command() done, defined at /usr/local/lib/python3.10/site-packages/redis/asyncio/connection.py:458>>
```

#### Sync

```
docker compose run test sync
```

```
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 529, in send_packed_command
    self.check_health()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 521, in check_health
    self.retry.call_with_retry(self._send_ping, self._ping_failed)
  File "/usr/local/lib/python3.10/site-packages/redis/retry.py", line 62, in call_with_retry
    return do()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 510, in _send_ping
    self.send_command("PING", check_health=False)
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 556, in send_command
    self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 526, in send_packed_command
    self.connect()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 369, in connect
    self.on_connect()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 463, in on_connect
    self.send_command("CLIENT", "SETNAME", self.client_name)
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 556, in send_command
    self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 529, in send_packed_command
    self.check_health()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 521, in check_health
    self.retry.call_with_retry(self._send_ping, self._ping_failed)
  File "/usr/local/lib/python3.10/site-packages/redis/retry.py", line 62, in call_with_retry
    return do()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 510, in _send_ping
    self.send_command("PING", check_health=False)
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 556, in send_command
    self.send_packed_command(
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 526, in send_packed_command
    self.connect()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 357, in connect
    sock = self.retry.call_with_retry(
  File "/usr/local/lib/python3.10/site-packages/redis/retry.py", line 62, in call_with_retry
    return do()
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 358, in <lambda>
    lambda: self._connect(), lambda error: self.disconnect(error)
  File "/usr/local/lib/python3.10/site-packages/redis/connection.py", line 698, in _connect
    for res in socket.getaddrinfo(
RecursionError: maximum recursion depth exceeded
```

### Poetry

```
docker compose run poetry lock
```
