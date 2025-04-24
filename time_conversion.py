import numpy as np
from datetime import timedelta

def minutes_to_hhmm(time_array):
    return np.array([str(timedelta(minutes=int(minute)))[:-3] for minute in time_array])


