# Manuel implementering af lineær regression
import numpy as np
import matplotlib.pyplot as plt

# Data: [alder (år), blodtryk (mmHg)] - flere datapunkter
x = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
y = np.array([110, 115, 118, 122, 128, 135, 140, 145, 150, 155, 160])

print("DATA:")
print(f"x (alder):    {x}")
print(f"y (blodtryk): {y}")

# Trin 1: Beregn middelværdier
x_mean = np.mean(x)
y_mean = np.mean(y)

print("\nTRIN 1: MIDDELVÆRDIER")
print(f"x̄ (gennemsnitsalder):    {x_mean:.1f} år")
print(f"ȳ (gennemsnitsblodtryk): {y_mean:.1f} mmHg")

# Trin 2: Beregn afvigelser fra middelværdi
x_diff = x - x_mean
y_diff = y - y_mean

print("\nTRIN 2: AFVIGELSER FRA MIDDELVÆRDI")
print(f"(x - x̄): {x_diff}")
print(f"(y - ȳ): {y_diff}")

# Trin 3: Beregn hældning (m)
numerator = np.sum(x_diff * y_diff)
denominator = np.sum(x_diff ** 2)
m = numerator / denominator

print("\nTRIN 3: BEREGN HÆLDNING (m)")
print(f"Tæller:   Σ(x-x̄)(y-ȳ) = {numerator:.1f}")
print(f"Nævner:   Σ(x-x̄)²      = {denominator:.1f}")
print(f"Hældning: m = {m:.4f} mmHg/år")

# Trin 4: Beregn skæring (b)
b = y_mean - m * x_mean

print("\nTRIN 4: BEREGN SKÆRING (b)")
print(f"b = ȳ - m·x̄")
print(f"b = {y_mean:.1f} - {m:.4f}·{x_mean:.1f}")
print(f"b = {b:.2f} mmHg")

# Resultat
print("\n" + "=" * 50)
print("RESULTAT")
print("=" * 50)
print(f"Regressionslinje: y = {m:.4f}x + {b:.2f}")
print(f"\nFortolkning:")
print(f"  - For hvert år ældre stiger blodtrykket {m:.4f} mmHg")
print(f"  - Ved alder 0 ville BT være {b:.2f} mmHg (ekstrapolation)")
print("=" * 50)

# Beregn forudsagte værdier
y_pred = m * x + b

# Plot data og regressionslinje
plt.figure(figsize=(10, 6))

# Scatter plot af faktiske data
plt.scatter(x, y, color='blue', s=100, alpha=0.7, label='Faktiske data', zorder=3)

# Regressionslinje
plt.plot(x, y_pred, color='red', linewidth=2.5, label=f'Regression: y = {m:.2f}x + {b:.1f}', zorder=2)

# Tilføj grid bag datapunkterne
plt.grid(True, alpha=0.3, linestyle='--', zorder=1)

# Labels og titel
plt.xlabel('Alder (år)', fontsize=12, fontweight='bold')
plt.ylabel('Systolisk blodtryk (mmHg)', fontsize=12, fontweight='bold')
plt.title('Lineær regression: Blodtryk vs Alder', fontsize=14, fontweight='bold', pad=15)

# Legend
plt.legend(fontsize=11, loc='lower right')

# Tilpas layout
plt.tight_layout()

# Gem figur
plt.savefig('regression_plot.png', dpi=300, bbox_inches='tight')
print("\nPlot gemt som 'regression_plot.png'")

# Vis plot
plt.show()

print("\nBemærk:")
print("  - Blå punkter viser de faktiske målinger")
print("  - Rød linje viser den beregnede regressionslinje")
print("  - Jo tættere punkterne er på linjen, jo bedre er fittet")