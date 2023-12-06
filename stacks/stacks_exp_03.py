# collections ---> deque()
# queue ---> Lifoqueue()

import collections
import queue


stack01 = collections.deque()
stack02 = queue.LifoQueue()

stack01.append(10)
stack02.put(5)

stack01.pop()
stack02.get()