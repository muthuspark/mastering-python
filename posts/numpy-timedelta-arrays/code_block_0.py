import numpy as np

timedeltas = np.array([1, 2, 3], dtype='timedelta64[D]')  #Days
print(timedeltas)

timedeltas_hours = np.array([1, 2, 3], dtype='timedelta64[h]') #Hours
print(timedeltas_hours)


#Creating from a list of strings
timedeltas_strings = np.array(['1D', '2D', '3D'], dtype='timedelta64')
print(timedeltas_strings)

#From a list of existing timedelta64 objects

import datetime
td_list = [datetime.timedelta(days=1), datetime.timedelta(days=2), datetime.timedelta(days=3)]
timedeltas_from_list = np.array(td_list)
print(timedeltas_from_list)