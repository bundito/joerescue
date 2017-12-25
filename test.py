import time
import signal

class Clockwork:
    def __init__(self, seconds):
        self.last_served = time.time()
        self.timeout = float(seconds)

    def timeout(self):
        self.curr_time = time.time()
        self.elapsed = self.curr_time - self.last_served
        if self.elapsed > self.timeout:


def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])