"""
Generate synthetic heart rate data for linear regression analysis.

Model:
HR = 140 - 0.8*Age + 5*Gender + noise

Where:
- HR: Heart Rate (bpm)
- Age: Age in years (0-80, includes infants to elderly)
- Gender: Numeric encoding - Female=0, Male=1 (males have ~5 bpm higher baseline HR)
- noise: Random normal variation (std varies by gender)
  * Female: std=0.3 bpm (lower variability)
  * Male: std=0.8 bpm (higher variability)

IMPORTANT: Gender encoding in CSV
  Female = 0
  Male   = 1

Realistic heart rates by age and gender:
At age 0 (newborn):
  - Female: ~140 bpm
  - Male: ~145 bpm
At age 20 (young adult):
  - Female: ~124 bpm
  - Male: ~129 bpm
At age 40 (middle-aged):
  - Female: ~108 bpm
  - Male: ~113 bpm
At age 70 (elderly):
  - Female: ~84 bpm
  - Male: ~89 bpm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================================
# GENDER ENCODING: Female = 0, Male = 1
# ============================================================================

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_samples = 3000

# Generate independent variables
age = np.random.uniform(0, 80, n_samples)  # Age 0-80 years (infants to elderly)
gender = np.random.randint(0, 2, n_samples)  # 0 = Female, 1 = Male

# Known model parameters
intercept = 140
coef_age = -0.8      # HR decreases by ~0.8 bpm per year of age
coef_gender = 5      # Males have ~5 bpm higher baseline HR than females

# Generate noise with different variability for males vs females
# Females: std=0.3 bpm (lower variability)
# Males: std=0.8 bpm (higher variability)
noise = np.where(gender == 0, 
                 np.random.normal(-2, 2, n_samples),  # Females: low variability
                 np.random.normal(-3, 3, n_samples))  # Males: high variability

# Calculate heart rate
heart_rate = intercept + coef_age * age + coef_gender * gender + noise

# Ensure heart rate is within reasonable bounds
heart_rate = np.clip(heart_rate, 40, 200)


# Create DataFrame with numeric gender first
data = pd.DataFrame({
    'age': age,
    'gender': gender,
    'heart_rate': heart_rate
})

# Create a copy for CSV output with gender labels
data_csv = data.copy()
#data_csv['gender'] = data_csv['gender'].map({0: 'Female', 1: 'Male'})

# Save to CSV with gender labels
output_file = 'synthetic_hr_data.csv'
data_csv.to_csv(output_file, index=False)

print(f"Generated {n_samples} samples of synthetic data")
print(f"Saved to: {output_file}")
print(f"\nData summary:")
print(data.describe())
print(f"\nModel used:")
print(f"HR = {intercept} + {coef_age}*Age + {coef_gender}*Gender + noise")
print(f"\nKey insights:")
print(f"  - Heart rate decreases ~{abs(coef_age)} bpm per year of age")
print(f"  - Males have ~{coef_gender} bpm higher baseline HR than females")
print(f"  - Female noise: std=0.3 bpm (lower variability)")
print(f"  - Male noise: std=0.8 bpm (higher variability)")
# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Heart Rate vs Age (colored by gender)
females = data[data['gender'] == 0]
males = data[data['gender'] == 1]
axes[0, 0].scatter(females['age'], females['heart_rate'], alpha=0.4, s=10, color='red', label='Female')
axes[0, 0].scatter(males['age'], males['heart_rate'], alpha=0.4, s=10, color='blue', label='Male')
axes[0, 0].set_xlabel('Age (years)')
axes[0, 0].set_ylabel('Heart Rate (bpm)')
axes[0, 0].set_title('Heart Rate vs Age (by Gender)')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Heart Rate distribution by gender
axes[0, 1].hist(females['heart_rate'], bins=30, alpha=0.6, label='Female', color='red', edgecolor='black')
axes[0, 1].hist(males['heart_rate'], bins=30, alpha=0.6, label='Male', color='blue', edgecolor='black')
axes[0, 1].set_xlabel('Heart Rate (bpm)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of Heart Rate by Gender')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Plot 3: Box plot by gender
axes[1, 0].boxplot([females['heart_rate'].values, males['heart_rate'].values], 
                    tick_labels=['Female (0)', 'Male (1)'])
axes[1, 0].set_xlabel('Gender')
axes[1, 0].set_ylabel('Heart Rate (bpm)')
axes[1, 0].set_title('Heart Rate Distribution by Gender')

# Plot 4: Age distribution
axes[1, 1].hist(data['age'], bins=40, edgecolor='black', alpha=0.7, color='green')
axes[1, 1].set_xlabel('Age (years)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Distribution of Ages')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('synthetic_hr_data_plot.png', dpi=100, bbox_inches='tight')
print("\nPlot saved to: synthetic_hr_data_plot.png")
plt.show()