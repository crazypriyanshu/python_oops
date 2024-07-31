from collections import defaultdict
import time


class Logger(object):
    timeStoreLength = 5 # Meaning you can store after this much time
    def __init__(self):
        self.timeToMessages = defaultdict(set)  # maps a time to set of messages printed at that time

    '''
    Returns true if the message should be printed in given timestamp otherwise return false
    Timestamp is in seconds granularity
    :type timestamp: int
    :type message: string
    :rtype: bool
    '''
    def shouldPrintMessage(self, timestamp, message):
        oldTimestamps = list(self.timeToMessages.keys())
        for oldTime in oldTimestamps:
            if timestamp - oldTime >= self.timeStoreLength:
                del self.timeToMessages[oldTime]
        for oldTime in self.timeToMessages:
            if message in self.timeToMessages[oldTime]:
                return False
        self.timeToMessages[timestamp].add(message)
        return True


obj = Logger()

for i in range(30):
    print("Start sleeping for a sec:", time.ctime())
    time.sleep(0.5)
    print("Wake up time:", time.ctime())
    print(i)
    print(f'${obj.shouldPrintMessage(i, "Hello + ${i}")}  ')
