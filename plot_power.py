# Hier soll die Powerkurve erstellt werden

import matplotlib.pyplot as plt
import numpy as np

def plot_power_curve(power_W, time_s):

    # Erstelle die Powerkurve
    plt.figure(figsize=(10, 6))
    plt.plot(time_s, power_W, label='Power Curve', color='blue')
    plt.title('Power Curve')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, len(power_W))  # Setze die x-Achse auf die Länge von sorted_power_W
    plt.ylim(0, np.max(power_W) * 1.1)  # Setze die y-Achse auf den maximalen Wert von power_W
    plt.show()  # Zeige die Powerkurve an
    

