from utils import root
from utils import loadfile

from names import NameFactory
from addresses import AddressFactory

import handlers
import settings

class Template(object):
    def __init__(self):
        self.name = NameFactory().generate()
        self.address = AddressFactory().generate()
        self.handlers = {}
        self.register(handlers)

        print self.name
        print self.address

    def register(self, handlers):
        ''' Registers the handlers in the specified module to the class. '''
        functions = [h for h in dir(handlers) 
                     if not h.startswith('__') 
                     and not h.endswith('__')]

        for f in functions:
            fn = eval('{}.{}'.format(handlers.__name__, f))
            if callable(fn):
                self.handlers[f.strip('_')] = fn

    def argparser(self, field):
        ''' Parses the function name and the arguments from the field value. '''
        field = field.strip("{}")
        if ':' in field:
            func, allargs = field.split(':')
            args = allargs.split(',')
        else:
            func, args = field, None
        return func, args

    def render(self, field):
        ''' Renders a field into a string element using a registered handler. '''
        func, args = self.argparser(field)
        if func in self.handlers:
            return self.handlers[func](self, args)
        return field

    def is_field(self, field):
        ''' Checks to see if a text string is a template field. '''
        try:
            return field.startswith('{') and field.endswith('}')
        except:
            return False

    def walk(self, template):
        ''' Recursive function to look through the dict and rendering template
        values. '''
        for key, value in template.items():
            if isinstance(value, dict):
                self.walk(value)
            elif self.is_field(value):
                template[key] = self.render(value)
            else:
                pass

    def parse(self):
        template = loadfile(settings.TEMPLATE, _format='json')
        self.walk(template)

        return template
