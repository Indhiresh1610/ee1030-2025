import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Define vectors from the problem ---
v1 = np.array([1, 0, 1])  # Changed from [1, 1, 1]
v2 = np.array([2, 3, 1])
v3 = np.array([5, 6, 4])

# Form a matrix with vectors as columns
matrix = np.column_stack((v1, v2, v3))

# Calculate the rank of the matrix
rank = np.linalg.matrix_rank(matrix)

print("--- Result from Native Python ---")
print(f"Matrix:\n{matrix}")
print(f"\nRank of the matrix: {rank}")

# --- 2. Create the plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors as arrows from the origin
origin = [0, 0, 0]
ax.quiver(*origin, *v1, color='r', label=f'v1: {v1}', arrow_length_ratio=0.1)
ax.quiver(*origin, *v2, color='g', label=f'v2: {v2}', arrow_length_ratio=0.1)
ax.quiver(*origin, *v3, color='b', label=f'v3: {v3}', arrow_length_ratio=0.1)

# --- 3. Check for dependence and plot plane ONLY if dependent ---
if rank < 3:
    print("Conclusion: The vectors are linearly dependent (coplanar).")
    ax.set_title('3D Visualization of Linearly Dependent Vectors')
    
    # The normal to the plane is the cross product of two of the vectors
    normal_vector = np.cross(v1, v2)

    # Create a grid for the plane surface plot
    x_range = np.linspace(0, 5, 10)
    y_range = np.linspace(0, 6, 10)
    xx, yy = np.meshgrid(x_range, y_range)

    # Calculate corresponding z values for the plane
    if normal_vector[2] != 0:
        zz = (-normal_vector[0] * xx - normal_vector[1] * yy) / normal_vector[2]
        ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray', rstride=100, cstride=100)
else:
    print("Conclusion: The vectors are linearly independent.")
    ax.set_title('3D Visualization of Linearly Independent Vectors')

# --- 4. Formatting the plot ---
max_val = np.max(np.abs(matrix)) * 1.1
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([0, max_val])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
ax.grid(True)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.353/figs/figure1.png")
plt.show()
