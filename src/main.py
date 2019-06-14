import sys
from datetime import datetime

from parametes_menu import ParametersMenu
from services.processor_service import ProcessorService

def main(argv):
  params = ParametersMenu(argv)
  cities = params.get('cities')
  debug = params.get('debug')
  pageSize = params.get('pageSize')
  threads = params.get('threads')
  processorService = ProcessorService(debug, pageSize, threads)
  processorService.process(cities)

if __name__ == '__main__':
  dataIni = datetime.now()
  try:
    main(sys.argv[1:])
  except Exception as ex:
    print(ex)
  print('Time spent routine: {}'.format(datetime.now() - dataIni))
