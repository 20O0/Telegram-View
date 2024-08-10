import requests
dyno = ‘DYNO’
class A:
 def der(self, url):
  for i in range(1, 8001):
   try:
    self.req = requests.get(url)
    if self.req.status_code == 200:
     print('done send view By {dyno} ')
    else:
     print('bad request')
   except Exception as e:
    print('weak wifi')
obj = A()
obj.der(str(input('enter url tele: ')))
