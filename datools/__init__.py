class colorcycle:
    cols = ['b','g','r', 'c', 'm', 'y', 'k']
    index = 0

    def current(self):
        return self.cols[(self.index+1) % len(self.cols)]

    def next(self):
        self.index += 1
        return self.cols[(self.index+1) % len(self.cols)]


class Enum(object):
    """Use to create enumerations 
    For example:
    >>> colors = Enum("Red", "Blue", "Green", "Yellow", "Purple")
    >>> colors.keys
    ('Red', 'Blue', 'Green', 'Yellow', 'Purple')
    >>> colors.Green
    2
    """
    def __init__(self, *keys):
        self.keys = keys
        self.__dict__.update(zip(keys, range(len(keys))))
    def value(self, key):
        return self.keys.index(key) 

def uniqify(seq):
    """
    Remove duplicates from seq while preserving order.
    """
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]
