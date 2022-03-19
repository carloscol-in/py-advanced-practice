import time


def log_generator(request):
    for i in range(10):
        if request.is_disconnected():
            print('Disconnected!')
            return

        yield i
        time.sleep(1)

class Request:

    def __init__(self):
        self.connected = True

    def is_disconnected(self):
        return self.connected == False

    def disconnect(self):
        if (self.connected):
            self.connected = False


if __name__ == "__main__":
    req = Request()

    lg = log_generator(req)

    print(next(lg))
    print(next(lg))
    print(next(lg))
    req.disconnect()
    print(next(lg))
