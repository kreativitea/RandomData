import os
import json

try:
    import yaml
except ImportError:
    yaml = None


def root():
    ''' Assuming that this function is in root.utils, returns the root directory
    of the project. '''
    path, _ = os.path.split(__file__)
    return os.path.abspath(path)


def loadfile(filename, _format=None):
    ''' Loads a file at a particular `filename` location. '''
    with open(filename) as file:
        data = file.read()

    if not _format:
        return data
    elif _format=='json':
        return json.loads(data)
    elif _format=='yaml':
        if yaml:
            return yaml.load(data)
        else:
            print "yaml support is not currently installed."
    elif _format=='split':
        return data.split()
