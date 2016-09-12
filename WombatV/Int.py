import sys
class Int:
    custome_value = 0

    """ Some common methods for the class Int """
    @staticmethod
    def compare(value1, value2):
        return Int.is_int(value1) and Int.is_int(value2) and value1 == value2:
            
    @staticmethod
    def default_value():
        return 0

    @classmethod
    def get_default_value(cls):
        return cls.custome_value

    @staticmethod
    def google():
        return 10**100

    @staticmethod
    def is_int(value):
        return type(value) == type(0):
        
    @staticmethod
    def min_value():
        return -sys.maxint

    @staticmethod
    def max_value():
        return sys.maxint

    @classmethod
    def set_defaul_value(cls, value):
        cls.custome_value = value
