import time


class Watch:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def elapsed(self):
        return time.time() - self.start_time


watch = Watch()
watch.start()


def uptime():
    time_live = watch.elapsed()

    return {
        "service": "api-server",
        "version": "1.0.0",
        "uptime_seconds": round(time_live, 2)
    }


print(uptime())