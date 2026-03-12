import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data (tværsnit, usorteret rækkefølge)
pulse_bpm = np.array([74, 61, 88, 69, 95, 57, 82, 76, 90, 64])
systolic_bp_mmhg = np.array([123, 110, 136, 118, 142, 106, 129, 124, 138, 113])

# Baseline-model (samme ide som i puls_bt_regression1.py)
regression_model = LinearRegression()
regression_model.fit(pulse_bpm.reshape(-1, 1), systolic_bp_mmhg)

# Modelparametre og R2
slope_mmhg_per_bpm = regression_model.coef_[0]
intercept_mmhg = regression_model.intercept_
r2_score = regression_model.score(pulse_bpm.reshape(-1, 1), systolic_bp_mmhg)

# Forudsigelser og residualer
predicted_systolic_bp_mmhg = regression_model.predict(pulse_bpm.reshape(-1, 1))
residuals_mmhg = systolic_bp_mmhg - predicted_systolic_bp_mmhg

residual_mean_mmhg = np.mean(residuals_mmhg)
residual_std_mmhg = np.std(residuals_mmhg)

print("MODELRESULTATER")
print("=" * 50)
print(f"Slope:                {slope_mmhg_per_bpm:.4f} mmHg/bpm")
print(f"Intercept:            {intercept_mmhg:.4f} mmHg")
print(f"R^2:                  {r2_score:.4f}")
print(f"Residual mean:        {residual_mean_mmhg:.4f} mmHg")
print(f"Residual std:         {residual_std_mmhg:.4f} mmHg")
print("=" * 50)

# Residualplots
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].scatter(predicted_systolic_bp_mmhg, residuals_mmhg, color="teal", s=70, alpha=0.8)
axes[0].axhline(0, color="black", linestyle="--", linewidth=1.5)
axes[0].set_xlabel("Forudsagt systolisk BT (mmHg)")
axes[0].set_ylabel("Residualer (mmHg)")
axes[0].set_title("Residualer vs forudsagt")
axes[0].grid(alpha=0.3)

axes[1].hist(residuals_mmhg, bins=6, color="slateblue", alpha=0.8, edgecolor="white")
axes[1].axvline(0, color="black", linestyle="--", linewidth=1.5)
axes[1].set_xlabel("Residualer (mmHg)")
axes[1].set_ylabel("Antal")
axes[1].set_title("Histogram af residualer")
axes[1].grid(alpha=0.3, axis="y")

plt.show()
