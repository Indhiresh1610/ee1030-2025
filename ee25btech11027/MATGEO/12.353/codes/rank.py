import ctypes
import os
import platform
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Determine library name and path ---
lib_name = 'rank.so' if platform.system() != 'Windows' else 'rank.dll'
lib_path = os.path.join(os.getcwd(), lib_name)

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library '{lib_name}': {e}")
    print("Please ensure you have compiled the corresponding C file in the same directory.")
    exit()

# --- Define the C function's signature for type safety ---
# Assuming the C function is named 'check_vectors'
c_lib.check_vectors.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
c_lib.check_vectors.restype = ctypes.c_int

# --- Main execution block ---
if __name__ == "__main__":
    print("This script checks if three predefined 3D vectors are linearly dependent.")

    v1_list = [1.0, 0.0, 1.0]
    v2_list = [2.0, 3.0, 1.0]
    v3_list = [5.0, 6.0, 4.0]

    # --- Part 1: C Function Call ---
    # Convert Python lists to C-compatible arrays
    V1_CArray = (ctypes.c_double * 3)(*v1_list)
    V2_CArray = (ctypes.c_double * 3)(*v2_list)
    V3_CArray = (ctypes.c_double * 3)(*v3_list)

    # Call the C function to get the result
    result_code = c_lib.check_vectors(V1_CArray, V2_CArray, V3_CArray)
    
    # --- Part 2: Display Result and Plot ---
    print("\n--- Analysis Result from C Function ---")
    # Assuming result_code 2 means dependent, and anything else means independent
    is_dependent = (result_code == 2)
    
    if is_dependent:
        print("The vectors are linearly dependent (coplanar).")
        print("Generating a 3D plot to visualize the vectors on their plane...")
    else:
        print("The vectors are linearly independent.")
        print("Generating a 3D plot of the vectors...")

    # Convert lists to NumPy arrays for plotting
    v1 = np.array(v1_list)
    v2 = np.array(v2_list)
    v3 = np.array(v3_list)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    origin = [0, 0, 0]
    ax.quiver(*origin, *v1, color='r', label=f'v1: {v1}', arrow_length_ratio=0.1)
    ax.quiver(*origin, *v2, color='g', label=f'v2: {v2}', arrow_length_ratio=0.1)
    ax.quiver(*origin, *v3, color='b', label=f'v3: {v3}', arrow_length_ratio=0.1)
    
    # This part of the code for plotting the plane will not run,
    # because these specific vectors are linearly independent.
    if is_dependent:
        normal_vector = np.cross(v1, v2)
        if np.linalg.norm(normal_vector) > 1e-6:
            x_range = np.linspace(min(0, v1[0], v2[0], v3[0]), max(v1[0], v2[0], v3[0]), 5)
            y_range = np.linspace(min(0, v1[1], v2[1], v3[1]), max(v1[1], v2[1], v3[1]), 5)
            xx, yy = np.meshgrid(x_range, y_range)
            
            if abs(normal_vector[2]) > 1e-6:
                zz = (-normal_vector[0] * xx - normal_vector[1] * yy) / normal_vector[2]
                ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray', rstride=100, cstride=100)

    # Formatting the plot
    max_range = np.max(np.abs([v1, v2, v3])) * 1.1
    ax.set_xlim([-1, 7])
    ax.set_ylim([-1, 7])
    ax.set_zlim([-1, 7])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Visualization of Linearly Independent Vectors')
    ax.legend()
    ax.grid(True)
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.353/figs/figure1.png")
    plt.show()
