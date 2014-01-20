import json
import pprint
from contextlib import closing

try:
    import requests
except ImportError:
    import urllib2
    requests = None

import settings

URL = 'http://{}:{}/'.format(settings.ENDPOINT, settings.PORT)

def requests_send(payload):
    ''' Sends a `POST` request using requsts. '''
    r = requests.post(URL,
                      data=json.dumps(payload),
                      headers=settings.HTTP_HEADERS,
                      auth=settings.AUTH,
                      verify=settings.SSL_VERIFY)

    print 'headers:\n {}'.format(pprint.pformat(r.headers))
    print ''
    print 'status code:\n {}'.format(pprint.pformat(r.status_code))
    print ''
    print 'content:\n {}'.format(r.content)


def urllib2_send(payload):
    ''' Sends a `POST` request using urllib2. '''
    data = json.dumps(payload)
    clen = len(data)
    headers = {'Content-Type': 'application/json', 'Content-Length': clen}
    req = urllib2.Request(URL, data, headers)
    with closing(urllib2.urlopen(req)) as f:
        response = f.read()
        print response


def send(payload):
    ''' Requests is the better library, but urlib2 is built in. '''
    if requests:
        requests_send(payload)
    else:
        urllib2_send(payload)
