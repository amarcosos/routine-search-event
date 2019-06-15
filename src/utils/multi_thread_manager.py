import multiprocessing
import time

class MultiThreadManager(multiprocessing.Process):
  THREAD_ID = 'THREADS'

  def __init__(self, target=None, args=None):
    multiprocessing.Process.__init__(self)
    self.target = target
    self.args = args

  def run(self):
    self.target(*self.args)

  # def process(self):
  #     t = multiprocessing.Process(target=self.target, args=self.args)
  #     # t.name = self.THREAD_ID
  #     # t.start()
  #     self.threads.append(t)
  #     return t

  def waitThemFinish(self, threads):
    for thread in threads:
      thread.join()

  def sleep(self):
    timeSleep = 0.2
    time.sleep(timeSleep)

def getCountRunning():
  return multiprocessing.active_children()

def getCpusNumber():
  return multiprocessing.cpu_count()
