import threading
import time
from queue import Queue

import constants


class Bucket(object):
    """令牌桶算法的实现类.

    每1/self.rate秒向桶内放一个令牌.
    每次请求从桶内取出一个令牌, 如果又令牌则取出，没有令牌则阻塞到有令牌，再取出令牌.
    """

    def __init__(self, max_size=constants.BUCKET_SIZE, rate=constants.RATE):
        self.max_size = max_size
        self.rate = rate
        self.queue = Queue(max_size)

    def auto_put(self):
        """开启一个Thread，每1/self.rate秒向桶内放一个令牌.
        :return: None.
        """
        def __run():
            while True:
                self.put()
                time.sleep(1 / self.rate)

        auto_put_thread = threading.Thread(target=__run)
        auto_put_thread.setDaemon(True)
        auto_put_thread.start()

    def put(self):
        """向桶内放一个令牌.

        :return: None.
        """
        self.queue.put(True)

    def get(self) -> object:
        """从桶内取一个令牌.

        如果桶内没有令牌，则阻塞到有令牌，再取出令牌.
        :return:
        """
        return self.queue.get()