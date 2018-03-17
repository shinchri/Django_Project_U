import threading


class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())


x = BuckyMessenger(name='Send out message')
y = BuckyMessenger(name='Receive message')

x.start()
y.start()