import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Provided data points
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([5.00, 3.62, 4.75, 3.91, 8.83, 16.18, 17.69])

# Fit a 7th degree polynomial
coefficients = np.polyfit(x, y, 7 - 1)
polynomial = Polynomial(coefficients)
print(polynomial)
# Generating a smooth curve for plotting
x_smooth = np.linspace(x.min(), x.max(), 500)
y_smooth = polynomial(x_smooth)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_smooth, y_smooth, label='7th Degree Polynomial Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('7th Degree Polynomial Regression')
plt.legend()
plt.grid(True)
plt.show()

coefficients
