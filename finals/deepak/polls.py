import requests
from pprint import pprint

base_url = 'http://elections.huffingtonpost.com/pollster/api/'

results = []
pollsters = []

# Charts

def get_charts():
  """
  valid topics are:

  obama-job-approval, 2016-president,
  2016-gop-primary, 2014-senate, 2014-house, 2014-governor,
  2013-senate, 2013-house, 2013-governor, 2012-senate,
  2012-president, 2012-house, 2012-governor, 2012-gop-primary
  """
  method = 'charts'
  payload = {
    # 'state' : 'NY',
    # 'topic' : '2016-president'
  }
  r = requests.get(base_url + method, params=payload)

  result = r.json()

  # Print all available charts
  chart_slugs = []
  for chart in result:
    chart_slugs.append(chart[u'slug'])
    print chart_slugs[-1]

  return chart_slugs

# Chart

def get_chart(slug):
  """
  Get specific chart. Get a list of all possible slugs by calling get_charts()
  """
  method = 'charts'
  r = requests.get(base_url + method + '/' + slug)

  result = r.json()
  pprint(result)

  return result


def collect_response(r, *args, **kwargs):
  """
  puts all the polls responses in a global list of 'results'
  """
  # print r.headers

  if r.status_code == requests.codes.ok:
    result = r.json()
    results.append(result)

    for polls in result:
      pollsters.append(polls[u'pollster'])
      print pollsters[-1]

def get_poll(page, topic):
  method = 'polls'
  payload = {
    'page' : str(page),
    # 'chart' : '',
    # 'state' : 'NY',
    # 'before' : '',
    # 'after' : '',
    # 'sort' : 'updated',
    'topic' : topic
  }
  r = requests.get(base_url + method, params=payload, hooks=dict(response=collect_response))


def get_2012_presidential_poll(pages):
  for page in range(1, pages):
    get_poll(page, '2012-president')
  print "\n\nThe results are stored in the global 'results' list for your convenience"

"""
Uncomment one at a time to see what kind of data the API provides
"""
get_charts()
# get_chart('2016-general-election-paul-vs-biden')
# get_2012_presidential_poll(6)
