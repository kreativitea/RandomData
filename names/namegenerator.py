import os
import random

import utils

def firstnames():
    filename = os.path.join(utils.root(), 'names', 'firstnames.csv')
    return utils.loadfile(filename, _format='split')
    

def lastnames():
    filename = os.path.join(utils.root(), 'names', 'lastnames.csv')
    return utils.loadfile(filename, _format='split')


class NameFactory(object):
    first = firstnames()
    last = lastnames()

    def generate(self, _format='dict'):
        ''' API level call.  If formatting has to happen, put it in here. '''
        if _format == 'dict':
            return self.name_info()
        elif _format == 'str':
            format_string = '{first} {middle} {last}'
            return format_string.format(**self.name_info())
        else:
            raise ValueError('format not recoginzed')

    def name_info(self):
        return {'first': random.choice(self.first),
                'middle': random.choice(self.first),
                'last': random.choice(self.first)}
