
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data (usorteret populationsrækkefølge)
pulse_bpm = np.array([74, 61, 88, 69, 95, 57, 82, 76, 90, 64])
systolic_bp_mmhg = np.array([123, 110, 136, 118, 142, 106, 129, 124, 138, 113])

# Fit model
regression_model = LinearRegression()
regression_model.fit(pulse_bpm.reshape(-1, 1), systolic_bp_mmhg)

# Parametre
slope_mmhg_per_bpm = regression_model.coef_[0]
intercept_mmhg = regression_model.intercept_
r2_score = regression_model.score(pulse_bpm.reshape(-1, 1), systolic_bp_mmhg)

# Forudsigelser på træningsdata
predicted_systolic_bp_mmhg = regression_model.predict(pulse_bpm.reshape(-1, 1))


print("RESULTATER")
print("=" * 40)
print(f"Slope:     {slope_mmhg_per_bpm:.4f} mmHg/bpm")
print(f"Intercept: {intercept_mmhg:.4f} mmHg")
# Ekstra forudsigelser
new_pulse_values_bpm = np.array([[0], [88]])
predicted_new_systolic_bp_mmhg = regression_model.predict(new_pulse_values_bpm)
for pulse_value, predicted_bp in zip(new_pulse_values_bpm.flatten(), predicted_new_systolic_bp_mmhg):
    print(f"Forudsagt systolisk BT ved puls {pulse_value}: {predicted_bp:.2f} mmHg")

# Plot
sorted_indices = np.argsort(pulse_bpm)
plt.figure(figsize=(8, 5))
plt.scatter(pulse_bpm, systolic_bp_mmhg, color="steelblue", s=70, alpha=0.85, label="Data")
plt.plot(
    pulse_bpm[sorted_indices],
    predicted_systolic_bp_mmhg[sorted_indices],
    color="darkorange",
    linewidth=2,
    label="Linear regression",
)
plt.xlabel("Puls (bpm)")
plt.ylabel("Systolisk blodtryk (mmHg)")
plt.title("Lineaer regression: puls vs systolisk blodtryk")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
