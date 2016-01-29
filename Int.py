import sys

class Int:
    value = 0
    customValue = 0

    @staticmethod
    def MinValue():
        return -sys.maxint

    @staticmethod
    def MaxValue():
        return -sys.maxint

    @staticmethod
    def Google():
        return 10**100

    @staticmethod
    def DefualValue():
        return Int.value

    @staticmethod
    def IsInt(value):
        if type(value) == type(Int.value):
            return True
        return False

    @staticmethod
    def Compare(value1, value2):
        if Int.IsInt(value1) and Int.IsInt(value2):
            if value1 == value2 :
                return True
            return False
        return None

    @staticmethod
    def SetDefaulValue(value):
        Int.customValue = value

    @staticmethod
    def GetDefaultValue():
        return Int.customValue

print ("El valor maximo es " + str(Int.Google()))
