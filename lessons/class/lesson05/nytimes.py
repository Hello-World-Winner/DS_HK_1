import requests

def get_nytimes(n):
  assert 31 > n
  base_url = 'http://stat.columbia.edu/~rachel/datasets/'
  csv_data = []
  header = ''
  for i in range(1,n+1):
    url = "%snyt%s.csv" % (base_url , str(i))
    print "Downloading ...%s [%d/%d]" % (url[-18:],i,n)
    data = requests.get(url).text.splitlines()
    header = data.pop(0)
    csv_data.extend(data)

  csv_data.insert(0, header)
  return csv_data

lines = get_nytimes(30)

with open('nytime.csv','w') as f:
  print 'Writing to file %s' % (f.name)
  for line in lines:
    f.write(line + "\n")
