import math as math
import matplotlib.pyplot as plt
import numpy as np

# Setting the plot
plt.title('Root Locus Analysis')
plt.grid()
plt.xlim(-80, 20)

# Step 1: Draw poles
poles = [0, -25, complex(-50, 10), complex(-50, -10)]
plt.scatter(np.real(poles), np.imag(poles), 50, "r", "x", label="Poles")

# Step 2: Draw the asymptotes with dotted lines
n = len(poles)  # Open loop poles
m = 0  # Open loop zeros
sigma = (sum(poles) - 0) / (n - m)
sigma = sigma.real  # Imaginary part must be zero

y_pos = 80 * math.sin(math.radians(180 / (n - m)))
x_pos = 80 * math.cos(math.radians(180 / (n - m)))
plt.plot([sigma, sigma + x_pos], [0, y_pos], color='black', linestyle='dashed', linewidth=0.5, label="Asymptotes")
plt.plot([sigma, sigma - x_pos], [0, y_pos], color='black', linestyle='dashed', linewidth=0.5)
plt.plot([sigma, sigma + x_pos], [0, -y_pos], color='black', linestyle='dashed', linewidth=0.5)
plt.plot([sigma, sigma - x_pos], [0, -y_pos], color='black', linestyle='dashed', linewidth=0.5)

# Step 3: Find and draw break away points
chs_eqn = np.poly(poles)
diff_chs_eqn = np.polyder(chs_eqn)
roots_diff_chs_eqn = np.roots(diff_chs_eqn)
break_away_points = []
for r in roots_diff_chs_eqn:
    if r.imag == 0:  # Add only real roots to break away points
        break_away_points.append(r)

zeros = np.zeros(len(break_away_points))
plt.scatter(break_away_points, zeros, 100, "g", "o", label="Break Points")

# Step 4: Find and draw the intersections with the imaginary axis using Routh
aux_roots = np.roots([-125 / 4580, 4580 * 65000 / 4580])
imag_inter = math.sqrt(aux_roots[0] / 4580)

plt.scatter([0, 0], [imag_inter, -imag_inter], 100, "y", "x", label="Imaginary Intersections")

# Step 5: Find and draw departure angles for complex poles
departure_angle = 180 - math.degrees(math.atan(10 / (-25))) - math.degrees(math.atan(10 / -50)) - 90

y_pos = 5 * math.sin(math.radians(180 - departure_angle))
x_pos = 5 * math.cos(math.radians(180 - departure_angle))
plt.plot([-50, -50 + 5], [10, 10], color='black', linestyle='dashed', linewidth=1)
plt.plot([-50, -50 - x_pos], [10, 10 + y_pos], color='black', linestyle='dashed', linewidth=1)
plt.plot([-50, -50 + 5], [-10, -10], color='black', linestyle='dashed', linewidth=1)
plt.plot([-50, -50 - x_pos], [-10, -10 - y_pos], color='black', linestyle='dashed', linewidth=1)

# Step 6: Draw the root locus
for k in np.linspace(-3000, 30000000, 500):
    chs_eqn[len(chs_eqn) - 1] += k
    roots = np.roots(chs_eqn)
    for r in roots:
        plt.scatter(r.real, r.imag, 10, "b")
    chs_eqn[len(chs_eqn) - 1] -= k

plt.plot([-20], [0], "bo", linewidth=0.1, label="Root locus")
degree = str(round(departure_angle, 4)) + '°'
plt.text(-50, 12, degree, fontsize=10)
plt.text(-50, -17, degree, fontsize=10)

plt.legend(loc="upper center")
plt.show()
