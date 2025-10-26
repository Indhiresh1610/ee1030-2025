import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Rank Method Calculation ---

# Define the coefficient matrix A
A = np.array([
    [2, -1, -1],
    [-1, 2, -1],
    [-1, -1, 2]
])

# Number of variables
n = A.shape[1]

# Calculate the rank of the matrix
rank_A = np.linalg.matrix_rank(A)

print(f"Coefficient Matrix A:\n{A}")
print(f"\nNumber of variables (n): {n}")
print(f"Rank of matrix A (ρ(A)): {rank_A}")

# Determine the number of solutions
if rank_A < n:
    print("\nConclusion: ρ(A) < n, so the system has an infinite number of solutions. ✅")
else:
    print("\nConclusion: ρ(A) = n, so the system has a unique solution (the trivial one).")

# --- Plotting the Graph ---

# Create a meshgrid for x and y coordinates
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Equations of the planes (solving for Z)
Z1 = 2*X - Y      # from 2x - y - z = 0
Z2 = -X + 2*Y     # from -x + 2y - z = 0
Z3 = (X + Y) / 2  # from -x - y + 2z = 0

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the three planes
ax.plot_surface(X, Y, Z1, alpha=0.5, label='2x - y - z = 0', color='r')
ax.plot_surface(X, Y, Z2, alpha=0.5, label='-x + 2y - z = 0', color='g')
ax.plot_surface(X, Y, Z3, alpha=0.5, label='-x - y + 2z = 0', color='b')

# Plot the line of intersection (x=y=z)
t = np.linspace(-10, 10, 100)
ax.plot(t, t, t, color='k', linewidth=4, label='Line of Intersection (x=y=z)')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Three Planes')
ax.view_init(elev=20, azim=-45) # Adjust viewing angle
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.561/figs/figure1.png")
plt.show()
