import json
import time
import sys

from math import ceil
from datetime import datetime, date, timedelta

from repositories.destination_repository import DestinationRepository
from repositories.source_repository import SourceRepository
from utils.multi_thread_manager import MultiThreadManager, getCountRunning
# from utils.thread_manager import ThreadManager

class ProcessorService():
  def __init__(self, debugMode, pageSize, threads):
    self.pageSize = pageSize
    self.threads = threads
    self.sourceRepository = SourceRepository()
    # self.threadManager = ThreadManager(debugMode)

  def process(self, cities):
    self._processData(cities)

  def _processData(self, cities):
    print('Starting routine\nStart: {}'.format(datetime.now()))

    for item in range(len(cities)):
      page_city = 1
      city = cities[item]
      total_pages = ceil(self.sourceRepository.getTotalSource(city, page_city))
      print('{} events in {}'.format(total_pages * 21, city))

      for index in range(total_pages):
        source = self.sourceRepository.getSource(city, page_city)

        if source:
          page_size = self._getPageSize(len(source))
          source_pages = self._getPagination(page_size, source)
          number_of_pages = len(source_pages)
          page = 0

          threads = []

          # MultiThread
          while page < number_of_pages:
            running = len(getCountRunning())
            if running < self.threads:
              print('Page {} of {}'.format((page + 1), number_of_pages))
              # self._processBlock(source_pages[page], page, number_of_pages)
              multiThreadManager = MultiThreadManager(target=self._processBlock, args=(source_pages[page], page, number_of_pages))
              threads.append(multiThreadManager)
              multiThreadManager.start()
              page += 1
            multiThreadManager.sleep()

          # Thread
          # while page < number_of_pages:
          #   running = len(getCountRunning())
          #   if running < self.threads:
          #     print('Page {} of {}'.format((page + 1), number_of_pages))
          #     thread = self.threadManager.start(target=self._processBlock, args=(source_pages[page], page, number_of_pages))
          #     threads.append(thread)
          #     page += 1
          #   self.threadManager.sleep()
          # self.threadManager.waitThemFinish(threads)
          page_city += 1
        else:
          print('No Data to process')
        print('End: {}'.format(datetime.now()))

  def _processBlock(self, sourcePages, page, numberOfPages):
    dic_destination = []

    for register in sourcePages:
      dic_source = {
        '_id': register.get('url').split('/')[3],
        'images': register.get('images'),
        'title': register.get('title').strip(),
        'local': {
          'name': register.get('location', {}).get('name', {}).strip().title(),
          'state': register.get('location', {}).get('state', {}).strip(),
          'city': register.get('location', {}).get('city', {}).strip().title(),
          'neighborhood': register.get('location', {}).get('neighborhood', {}).strip().title(),
          'address_alt': register.get('location', {}).get('address_alt', {}).strip().title(),
          'address': register.get('location', {}).get('address', {}).strip().title(),
          'address_num': register.get('location', {}).get('address_num', {}),
          'zip_code': register.get('location', {}).get('zip_code', {}),
          'lat': register.get('location', {}).get('lat', {}),
          'lon': register.get('location', {}).get('lon', {}),
        },
        'startDate': register.get('start_date'),
        'endDate': register.get('end_date'),
        'durationType': register.get('duration_type').strip(),
        'eventType': register.get('event_type').strip(),
        'url': register.get('url')
      }
      dic_destination.append(dic_source)

    if len(dic_destination) > 0:
      try:
        time.sleep(1)
        destinationRepository = DestinationRepository()
        destinationRepository.insertMany(dic_destination)
      except:
        try:
          time.sleep(3)
          destinationRepository = DestinationRepository()
          destinationRepository.insertMany(dic_destination)
        except:
          time.sleep(5)
          destinationRepository = DestinationRepository()
          destinationRepository.insertMany(dic_destination)
      dic_destination = []

  def _getPageSize(self, lenRegisters):
    reason = int(ceil(float(lenRegisters) / self.threads))
    page_size = self.pageSize if reason > self.pageSize else reason
    return page_size

  def _getPagination(self, pageSize, registers):
    chunk_registers = [registers[i:i+pageSize] for i in range(0, len(registers), pageSize)]
    return chunk_registers
