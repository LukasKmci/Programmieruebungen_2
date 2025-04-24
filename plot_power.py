# Hier soll die Powerkurve erstellt werden

import matplotlib.pyplot as plt
import numpy as np

def plot_power_curve(power_W, time_s):

    tick_spacing = 300  # 5 Minuten in Sekunden
    tick_positions = np.arange(0, len(time_s), tick_spacing)

    # Erstelle die Powerkurve
    #plt.figure(figsize=(10, 6))
    plt.plot(time_s, power_W, label='Power Curve', color='red')
    plt.title('Power Curve')
    plt.xlabel('Time (mm:ss)')
    plt.ylabel('Power (W)')
    plt.grid(True)
    plt.legend()
    plt.xlim(time_s[0], time_s[-1])  # Setze die x-Achse auf die Länge von sorted_power_W
    plt.ylim(0, np.max(power_W) * 1.1)  # Setze die y-Achse auf den maximalen Wert von power_W
    plt.xticks(ticks=tick_positions, labels=[time_s[i] for i in tick_positions])
    plt.savefig('figures/power_curve.png')  # Speichere die Powerkurve als PNG-Datei
    plt.show()  # Zeige die Powerkurve an

