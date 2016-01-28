#https://msdn.microsoft.com/es-es/library/system.string(v=vs.110).aspx

class String:
    value = ""
    customValue = ""

    @staticmethod
    def Empty():
        return String.value

    @staticmethod
    def IsEmpty(value):
        if value == String.Value:
            return True
        return False

    @staticmethod
    def IsNullOrEmpty(value):
        if Value == String.Value or Value == None:
            return True
        return False

    @staticmethod
    def SetDefaultValue(value):
        String.customValue = value

    @staticmethod
    def GetValue():
        return String.customValue

    @staticmethod
    def IsString(value):
        typeValue = type(value)
        typeString = type(String.value)

        if typeString == typeValue:
            return True
        return False

    @staticmethod
    def Compare(value1, value2):
        if IsValidValues(value1, value2):
            if value1 == value2:
                return True
            return False
        return False


    @staticmethod
    def Concat(*values):
        finalString = String.value
        for v in values:
            finalString = "{0} {1}".format(finalString, str(v))
        return finalString

    #Metodos Conctar indefinido with for
    @staticmethod
    def GetHasCode(value):
        return "code"

    @staticmethod
    def IndexOf(value, index):
        try:
            return value[index]
        except Exception as e:
            return None

    @staticmethod
    def Any(value1, value2):
        return True #Por concluir

    @staticmethod
    def GetLastIndex(value):
        if String.IsString(value):
            return  value[-1]

    @staticmethod
    def GetLastFirts(value):
        if String.IsString(value):
            return  value[0]

    @staticmethod
    def GetChainToIndex(value, index):
        if String.IsString(value):
            return value[index:]

    @staticmethod
    def RemoveToIndex(value1, index):
        if IsValidValues(value1):
            finalValue = String.value
            for i in range(0,len(value1)):
                if i != index:
                    finalValue += value1[i]
            return finalValue

    @staticmethod
    def Count(value):
        return len(value)

    @staticmethod
    def Count(value1, value2):
        if IsValidValues(value1, value2):
            pass
        return None

    @staticmethod
    def IsValidValues(*values):
        flag = True
        for value in values:
            if String.IsString(value) == False:
                return False
        return flag

valor = String.Empty()
print ("Concat  : " + str(String.Concat("Eduardo", 4, "Lalo", "Eddad")) )
