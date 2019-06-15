import getopt
from datetime import datetime, timedelta

def ParametersMenu(argv):
  try:
    params = {
      'cities': [ 'belo-horizonte-mg', 'brasilia-df', 'florianopolis-sc', 'goiania-go', 'rio-de-janeiro-rj', 'porto-alegre-rs', 'recife-pe', 'salvador-ba', 'sao-paulo-sp' ],# '/belo-horizonte-mg',
      'date': {
        'startDate': (datetime.today() - timedelta(days = 30)).strftime('%Y-%m-%d'),
        'endDate': (datetime.today() - timedelta(days = 0)).strftime('%Y-%m-%d')
      },
      'debug': False,
      'pageSize': 10000,
      'threads': 8
    }
    options, args = getopt.getopt(argv, 'q:hc:t:p:', ['help', 'days=', 'debug', 'max-threads=', 'page-size='])
    if (not options):
      raise NameError('Parameters must be entered')
  except Exception as e:
    print('Parameters were not entered correctly')
    print('Use:')
    print('-h (for help)')
    raise (e)
  for opt, arg in options:
    if opt in ('-h', '--help'):
      print('To run the routine use')
      print('Ex: routine.sh -c 1 ')
    elif opt in ('--max-threads'):
      params['threads'] = int(arg)
    elif opt in ('--page-size'):
      params['pageSize'] = int(arg)
    elif opt in ('--debug'):
      params['debug'] = True
    elif opt in ('-q','--days'):
      params['date']['startDate'] = (datetime.today() - timedelta(days = int(arg))).strftime('%Y-%m-%d')
  return params
