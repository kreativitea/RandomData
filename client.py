import json
import pprint

import requests

import settings


def send(payload):
    endpoint = 'http://{}:{}/'.format(settings.ENDPOINT, settings.PORT)

    r = requests.post(endpoint,
                      data=json.dumps(payload),
                      headers=settings.HTTP_HEADERS,
                      auth=settings.AUTH,
                      verify=settings.SSL_VERIFY)

    print 'headers:\n {}'.format(pprint.pformat(r.headers))
    print ''
    print 'status code:\n {}'.format(pprint.pformat(r.status_code))
    print ''
    print 'content:\n {}'.format(r.content)
