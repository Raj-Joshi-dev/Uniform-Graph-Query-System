import time


class ExecutionTimer:

    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        print("Total query execution time = ", time.time() - self.start_time, "ms")
        return time.time() - self.start_time
