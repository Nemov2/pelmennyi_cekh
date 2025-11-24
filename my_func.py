def mashineCount(mashineCapasity, lineCapacity):
    return lineCapacity/mashineCapasity

def pelmenMashineCount(qDay, t, pelmenMashineCapacity):
    pelmenLineCapacity = qDay/(2*t)
    return mashineCount(pelmenMashineCapacity, pelmenLineCapacity)

def testoMashineCount(qDay, testoPart, testoMashineCapacity):
    testoLineCapacity = (testoPart*qDay)/100
    return mashineCount(testoMashineCapacity, testoLineCapacity)

def meatMashineCount(qDay, testoPart, meatMashineCapacity):
    meatLineCapacity = ((100-testoPart)*qDay)/100
    return mashineCount(meatMashineCapacity, meatLineCapacity)