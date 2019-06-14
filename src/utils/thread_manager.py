import threading
import time

class ThreadManager():
  THREAD_ID = 'THREADS'

  def __init__(self, debugMode = False):
    self.threads = []
    self.debugMode = debugMode

  def start(self, target, args):
    if self.debugMode:
      return target(*args)
    else:
      t = threading.Thread(target = target, args = args)
      t.start()
      t.setName(self.THREAD_ID)
      self.threads.append(t)
      return t

  def countActiveThreads(self):
    response = len(filter(lambda x: x.getName() == self.THREAD_ID, threading.enumerate()))
    return response

  def sleep(self):
    sleepTime = 0.1
    time.sleep(sleepTime)

  def waitThemFinish(self):
    for thread in self.threads:
      thread.join()
