from WombatV import String, Int

def Repeat(value, chain):
    defaultInt = 0
    count = defaultInt
    if not String.Any(value, chain):
        return count

    for i in range(defaultInt,len(value)):
        if String.Any( value[i:i + len(chain)],  chain):
            count += 1
    return count

def MoreCommun(value):
    finalWord = String.Empty()
    finalRepeat = 0

    for w in value.split(" "):
        r = String.Repeat(value, w) - 1
        if r > finalRepeat:
            finalWord, finalRepeat = w, r
    return [finalWord, finalRepeat]

repeat = MoreCommun("Eduardo es una de las personas que se quieren superar en esta vida, como por ejemplo en en en")
print repeat
