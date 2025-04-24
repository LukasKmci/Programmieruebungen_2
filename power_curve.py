from load_data import load_data
from plot_power import plot_power_curve
from sort import bubble_sort
import numpy as np
from time_conversion import minutes_to_hhmm

# Hier soll die Powerkurve gespeichert werden

# load_data('activity.csv')
data = load_data('activity.csv')
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)

# Convert time to hh:mm format
time = np.array(range(len(sorted_power_W)))
#time = minutes_to_hhmm(time)

# plot
plot_power_curve(sorted_power_W, time)

# Save the plot as a PNG file
