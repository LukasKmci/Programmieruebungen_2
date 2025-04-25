# Hier soll die Powerkurve erstellt werden

import matplotlib.pyplot as plt
import numpy as np

def plot_power_curve(power_W, time_s):

    tick_spacing = 300  # 5 Minuten in Sekunden
    tick_positions = np.arange(0, len(time_s), tick_spacing)

    # Erstelle die Powerkurve
    #plt.figure(figsize=(10, 6))
    plt.plot(time_s, power_W, label='Power Curve', color='red', linewidth=2)
    plt.fill_between(time_s, power_W, color='lightcoral', alpha=0.5)  # Add shadow under the curve
    plt.title('Power Curve', fontsize=16, fontweight='bold')
    plt.xlabel('Time (mm:ss)', fontsize=12)
    plt.ylabel('Power (W)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12, loc='upper right')
    plt.xlim(time_s[0], time_s[-1])  # Set the x-axis to the length of time_s
    plt.ylim(0, np.max(power_W) * 1.1)  # Set the y-axis to slightly above the max value of power_W
    plt.xticks(ticks=tick_positions, labels=[time_s[i] for i in tick_positions], rotation=45, fontsize=10)
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.savefig('figures/power_curve.png', dpi=300, bbox_inches='tight')  # Save the Power Curve as a high-quality PNG file
    plt.show()  # Display the Power Curve

