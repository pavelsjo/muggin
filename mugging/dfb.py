import pandas as pd
import numpy as np
import names

def namesDt():
    pass

def testOne():
    normAge = pd.DataFrame({"ID" : np.random.randint(1111,3333, size=70),'Age' : np.random.randint(18,60, size=70)}) # Expected age range
    lowAge = pd.DataFrame({"ID" : np.random.randint(4444,5555, size=15),'Age' : np.random.randint(5,15, size=15)}) # Unexpected low ages range (caused by human mistakes)
    highAge = pd.DataFrame({"ID" : np.random.randint(6666,7777, size=15),'Age' : np.random.randint(55,110, size=15)}) # Unexpected high ages range (caused by human mistakes)
    s = pd.DataFrame() # It's our random ages container.
    return s.append([normAge,lowAge,highAge], ignore_index=True)