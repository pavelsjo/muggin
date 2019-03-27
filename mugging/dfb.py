import pandas as pd
import numpy as np
import names

def name_usuarios(num_users):
    '''EXAMPLES
    nombres_aleatorios = name_usuarios(200)
    nombres_aleatorios.head(3)'''
    table_aux = []
    df = pd.DataFrame()
    for row in range(num_users):
        table_aux.append(names.get_full_name())
    df = pd.DataFrame(table_aux)
    df.columns = ['names']
    return df

def data_usuarios():
    '''EXAMPLES
    datos_aleatorios = data_usuarios()
    datos_aleatorios.head(3)'''
    normAge = pd.DataFrame({"DNI" : np.random.randint(11111111,99999999, size=70),'Age' : np.random.randint(18,60, size=70)}) # Expected age range
    lowAge = pd.DataFrame({"DNI" : np.random.randint(11111111,99999999, size=15),'Age' : np.random.randint(5,15, size=15)}) # Unexpected low ages range (caused by human mistakes)
    highAge = pd.DataFrame({"DNI" : np.random.randint(11111111,99999999, size=15),'Age' : np.random.randint(55,110, size=15)}) # Unexpected high ages range (caused by human mistakes)
    s = pd.DataFrame() # It's our random ages container.
    return s.append([normAge,lowAge,highAge], ignore_index=True)

#EXAMPLES
#bd_usuarios = pd.concat([nombres_aleatorios,datos_aleatorios],axis=1)
#bd_usuarios.head(10)