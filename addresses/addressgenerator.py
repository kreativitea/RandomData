import os
import ast
import json
import random

import utils


def city_data():
    filename = os.path.join(utils.root(), 'addresses', 'cityinfo.json')
    return utils.loadfile(filename, _format='json')


class AddressFactory(object):
    data = city_data()

    def generate(self, _format='dict'):
        ''' API level call.  If formatting has to happen, put it in here. '''
        if _format == 'dict':
            return self.address_info()
        elif _format == 'str':
            format_string = '{address}, {city}, {state} {zip}'
            return format_string.format(**self.address_info())
        else:
            raise ValueError('format not recoginzed')

    def street_number(self):
        ''' Generates a random street number. '''
        return random.randint(1, 10**random.randint(1, 4) - 1)

    def street_type(self):
        ''' Returns a random street type. '''
        return random.choice(['Blvd.', 'Ave.', 'Ln.', 'Ct.', 'St.'])

    def street(self, info):
        ''' Returns a random street from an info object. '''
        return random.choice(info['streets'])

    def address_info(self):
        ''' Returns a dict of data. '''
        info = random.choice(self.data)
        address = '{} {} {}'.format(self.street_number(),
                                    self.street(info),
                                    self.street_type())

        return {'city': info.get('city'), 
                'state': info.get('state'),
                'zip': str(info.get('zip')), 
                'address': address}
