import ctypes
import platform
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Part 1: C Library Interaction ---

# Define matrix dimensions to match the C code
ROWS, COLS = 3, 3

# Determine library file name based on OS
lib_name = 'code.so' if platform.system() != 'Windows' else 'rank_calculator.dll'

try:
    c_lib = ctypes.CDLL('./' + lib_name)
except OSError:
    print(f"Error: Could not load the C library '{lib_name}'.")
    print("Please ensure you have compiled 'rank_calculator.c' first.")
    exit()

# Set up the function signature for ctypes
c_calculate_rank = c_lib.calculate_rank
C_Matrix = (ctypes.c_double * COLS) * ROWS
c_calculate_rank.argtypes = [C_Matrix]
c_calculate_rank.restype = ctypes.c_int

# Define the specific matrix for the problem
py_matrix = [
    [2.0, -1.0, -1.0],
    [-1.0, 2.0, -1.0],
    [-1.0, -1.0, 2.0]
]

# Convert the Python list into a C-compatible 2D array
c_matrix_instance = C_Matrix()
for i, row in enumerate(py_matrix):
    for j, val in enumerate(row):
        c_matrix_instance[i][j] = val

# Call the C function to get the rank
rank_A = c_calculate_rank(c_matrix_instance)
num_variables = 3

# Print the analysis
print("--- Analysis using Imported C Function ---")
print(f"Matrix passed to C:\n{np.array(py_matrix)}")
print(f"\nRank calculated by C function (ρ(A)): {rank_A}")
print(f"Number of variables (n): {num_variables}")

if rank_A < num_variables:
    print("\nConclusion: ρ(A) < n, so the system has an infinite number of solutions. ✅")
else:
    print("\nConclusion: ρ(A) = n, so the system has a unique solution.")

# --- Part 2: 3D Plotting ---

print("\nGenerating 3D plot...")
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a grid of x, y points
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Equations of the planes, solved for z
Z1 = 2*X - Y      # from 2x - y - z = 0
Z2 = -X + 2*Y     # from -x + 2y - z = 0
Z3 = (X + Y) / 2  # from -x - y + 2z = 0

# Plot the three planes
ax.plot_surface(X, Y, Z1, alpha=0.6, color='r', label='2x - y - z = 0')
ax.plot_surface(X, Y, Z2, alpha=0.6, color='g', label='-x + 2y - z = 0')
ax.plot_surface(X, Y, Z3, alpha=0.6, color='b', label='-x - y + 2z = 0')

# Plot the line of intersection (x=y=z) where the infinite solutions lie
t = np.linspace(-10, 10, 100)
ax.plot(t, t, t, color='black', linewidth=5, label='Line of Intersection (x=y=z)')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Planes for the System of Equations')
ax.view_init(elev=25, azim=-50) # Adjust viewing angle

# Show the plot
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.561/figs/figure1.png")
plt.show()
