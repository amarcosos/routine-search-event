import json
import re
import sys

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlopen

class SourceRepository():
  def __init__(self):
    self.url = 'https://www.sympla.com.br/eventos' # 'https://www.sympla.com.br/maratona-saudavel__533452'

  def getSource(self, city, page):
    params = '{}?ordem=data&pagina={}'.format('/{}'.format(city) if city else '', page)
    response = self._getPagination(params)
    return response.get('events', {})

  def getTotalSource(self, city, page):
    params = '/{}'.format(city) if city else ''
    response = self._getPagination(params)
    total_items = response.get('events_in_search')
    total_items_page = response.get('params', {}).get('limit')
    return total_items / total_items_page if total_items else 0

  def _getPagination(self, params):
    dic = {}
    web = urlopen('{}{}'.format(self.url, params))
    soup = BeautifulSoup(web.read(), 'lxml')
    scripts = soup.find_all('script')
    pattern = re.compile('var _search_params = (.*?);')
    
    # script = scripts[24].string
    # pattern1 = re.compile('_tracking_callback(.*?);')
    # data = pattern1.match(script)
    # event = json.loads(data.groups()[0])
    # print(event)
    
    for script in scripts:
      if(pattern.match(str(script.string))):
        data = pattern.match(script.string)
        event = json.loads(data.groups()[0])
        dic = event

    return dic
