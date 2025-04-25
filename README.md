# 📊 Programmierübungen 2 – Power Curve Projekt

Ein kleines Python-Projekt zur Analyse und Visualisierung von Leistungsdaten. Ziel ist es, aus Rohdaten (`activity.csv`) eine Leistungskurve zu berechnen und als Bild zu speichern.

---

## 👥 Contributors
- Simon Krainer  
- Lukas Köhler

---

## ⚙️ Installation mit [PDM](https://pdm.fming.dev/)

1. Öffne PowerShell oder Terminal
2. Wechsle in deinen Projektordner:
   ```bash
   cd dein-projektordner
   ```
3. Initialisiere das Projekt mit PDM:
   ```bash
   pdm init
   ```
4. Installiere die benötigten Pakete:
   ```bash
   pdm add matplotlib numpy pandas
   ```

---

## 🧠 Projektübersicht

| Datei                    | Beschreibung                                          |
|-------------------------|-------------------------------------------------------|
| `activity.csv`          | Rohdaten für die Analyse                              |
| `load_data.py`          | Liest die CSV-Datei ein                               |
| `sort.py`               | Sortiert die Daten mittels Bubble Sort                |
| `power_curve.py`        | Berechnet die Leistungskurve                          |
| `plot_power.py`         | Visualisiert die Leistung und speichert sie als PNG   |
| `figures/power_curve.png` | Ergebnisgrafik der Leistungskurve                    |
| `power_curve.py`               | Steuert den gesamten Ablauf                           |

---

## 🔁 Datenfluss

```mermaid
flowchart LR
    CSV["CSV-Datei"] -->|load_data| PowerOriginal
    PowerOriginal -->|sort / bubble_sort| SortedPower
    SortedPower -->|plot_power| Plot
    Plot -->|save_plot| Save
    Save --> PNG["figures/powercurve.png"]
```

---

## 📈 Beispielausgabe

![Power Curve](https://github.com/user-attachments/assets/39afd52c-6804-45fe-ab8b-73e5eefe4060)
