import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pylab as plt

puls =np.array([74, 61, 88, 69, 95, 57, 82, 76, 90, 64]).reshape(-1,1)
systolisk_blodtryk = np.array([123, 110, 136, 118, 142, 106, 129, 124, 138, 113])
print(puls.shape, systolisk_blodtryk.shape)
model = LinearRegression()
model.fit(puls,systolisk_blodtryk)
m = model.coef_[0]
b = model.intercept_

print("y =",m,"mmHg/bpm +", b, "mmHg")

pred_y = model.predict(np.array([[0],[88]]))

plt.scatter(puls,systolisk_blodtryk,label="raw data")
plt.plot(np.array([[0],[88]]),pred_y, color="r")
plt.show()

