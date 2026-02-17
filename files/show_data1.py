import numpy as np
import matplotlib.pyplot as plt

# Load the data using numpy with structured array
data = np.genfromtxt('synthetic_hr_data.csv', delimiter=',', skip_header=1, 
                      dtype='float,float,float', names='age,gender,heart_rate')

# Extract columns
age = data['age']
gender = data['gender']  # 0 = Female, 1 = Male
heart_rate = data['heart_rate']

# Print data summary
print(f"Total samples: {len(data)}")
print(f"\nFirst 10 rows:")
print(f"{'Age':<10} {'Gender':<10} {'Heart Rate':<12}")
print("-" * 32)
for i in range(min(10, len(data))):
    gender_label = 'Female' if gender[i] == 0 else 'Male'
    print(f"{age[i]:<10.1f} {gender_label:<10} {heart_rate[i]:<12.1f}")

# Separate heart rates by gender
females = heart_rate[gender == 0]
males = heart_rate[gender == 1]

print(f"\nFemales: n={len(females)}, mean={females.mean():.1f}, std={females.std():.1f}")
print(f"Males: n={len(males)}, mean={males.mean():.1f}, std={males.std():.1f}")

# Plot boxplot of heart rates by gender
plt.figure(figsize=(10, 6))
plt.boxplot([females, males], tick_labels=['Female', 'Male'], vert=True)
plt.title('Boxplot of Heart Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Heart Rate (bpm)')
plt.grid(True, alpha=0.3)
plt.show()