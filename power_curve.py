from load_data import load_data
from plot_power import plot_power_curve
from sort import bubble_sort
import numpy as np
from datetime import timedelta

# Hier soll die Powerkurve gespeichert werden

# load_data('activity.csv')
data = load_data('activity.csv')
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)

# Convert time to mm:ss format
time = np.arange(len(sorted_power_W))
time = [str(timedelta(seconds=int(s))).zfill(8)[-5:] for s in time]

# plot
plot_power_curve(sorted_power_W, time)