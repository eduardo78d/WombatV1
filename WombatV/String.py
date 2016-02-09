class String:
    value = ""
    customValue = ""
    space = " "

    @staticmethod
    def Any(value, chain):
        if chain in value:
            return True
        return False

    @staticmethod
    def Concat(*values):
        finalString = String.value
        for v in values:
            finalString = "{0} {1}".format(finalString, str(v))
        return finalString

    @staticmethod
    def Count(value):
        return len(value)

    @staticmethod
    def Compare(value1, value2):
        if String.IsValidValues(value1, value2):
            if value1 == value2:
                return True
            return False
        return None

    @staticmethod
    def CompareValues(*values):
        for v in values:
            if v != values[0]:
                return False
        return True

    @staticmethod
    def Copy(value):
        finalValue = String.value
        for v in value:
            finalValue += v
        return finalValue

    @staticmethod
    def Empty():
        return String.value

    @staticmethod
    def EndsWith(value, chain):
        if String.IsValidValues(value):
            if value[ len(value)-1] == str(chain):
                return True
            return False
        return None

    #Metodos Conctar indefinido with for
    @staticmethod
    def GetHasCode(value):
        return "code"

    @staticmethod
    def GetDefaultValue():
        return String.customValue

    @staticmethod
    def GetLastIndex(value):
        if String.IsString(value):
            return  value[-1]

    @staticmethod
    def GetFirtsIndex(value):
        if String.IsString(value):
            return  value[0]

    @staticmethod
    def MoreCommonWord(value):
        finalWord = String.Empty()
        finalRepeat = 0

        for w in value.split(" "):
            r = String.Repeat(value, w) - 1
            if r > finalRepeat:
                finalWord, finalRepeat = w, r
        return [finalWord, finalRepeat]

    @staticmethod
    def MoreCommonsWord(value, number): #Refactor
       pass

    @staticmethod
    def GetChainToIndex(value, index):
        if String.IsString(value):
            return value[index:]

    @staticmethod
    def IndexOf(value, index):
        try:
            return value[index]
        except Exception as e:
            return None

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
    def IsString(value):
        if type(value) == type(String.value):
            return True
        return False

    @staticmethod
    def IsValidValue(value):
        return String.IsValidValues(value)

    @staticmethod
    def IsValidValues(*values):
        flag = True
        for value in values:
            if not String.IsString(value):
                return False
        return flag

    @staticmethod
    def RemoveToIndex(value1, index):
        if String.IsValidValues(value1):
            finalValue = String.value
            for i in range(0,len(value1)):
                if i != index:
                    finalValue += value1[i]
            return finalValue

    @staticmethod
    def Repeat(value, chain):
        defaultInt = 0
        count = defaultInt
        if not String.Any(value, chain):
            return count

        for i in range(defaultInt,len(value)):
            if String.Any( value[i:i + len(chain)],  chain):
                count += 1
        return count

    @staticmethod
    def SetDefaultValue(value):
        String.customValue = value

    @staticmethod
    def StartWith(value, chain):
        if String.IsValidValues(value):
            if value[0] == str(chain):
                return True
            return False
        return None
