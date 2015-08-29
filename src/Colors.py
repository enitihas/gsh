__author__ = 'enitihas'

class Colors:
    map = dict( HEADER = '\033[95m',
    BLUE = '\033[94m',
    GREEN = '\033[92m',
    YELLOW = '\033[93m',
    RED = '\033[91m',
    END = '\033[0m',
    BOLD = '\033[1m',
    UNDERLINE = '\033[4m', )

    @classmethod
    def print(cls,color,stmt):
        print(cls.map[color] + stmt + cls.map['END'])
