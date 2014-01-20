import random


def name(cls, args):
    ''' Handler.  Returns the specified name. '''
    if not args:
        return '{first} {middle} {last}'.format(**cls.names)
    else:
        return ' '.join([cls.name[arg] for arg in args])


def _range(cls, args):
    ''' Handler.  Wrapper for the `range` function. '''
    args = [int(a) for a in args]
    return str(random.choice(range(*args)))


def choice(cls, args):
    ''' Handler.  Wrapper for the `random.choice` function. '''
    return str(random.choice(args))


def address(cls, args):
    ''' Handler.  Returns the specified portion of the address. '''
    return ' '.join([cls.address[arg] for arg in args])
