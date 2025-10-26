import ctypes
import platform
import numpy as np

# --- Part 1: Load the C Library and Set Up the Function ---

# Define matrix dimensions
SIZE = 3

# Load the compiled shared library
lib_name = 'code.so' if platform.system() != 'Windows' else 'eigen_calculator.dll'
try:
    c_lib = ctypes.CDLL('./' + lib_name)
except OSError as e:
    print(f"Error: Could not load C library '{lib_name}'.")
    print("Please make sure you have compiled the 'eigen_calculator.c' file first.")
    exit()

# Get the function from the library
c_find_eigenvalues = c_lib.find_eigenvalues

# Define the C-compatible types for the function's arguments
C_Matrix = (ctypes.c_double * SIZE) * SIZE
C_EigenvaluesArray = ctypes.POINTER(ctypes.c_double)

# Specify the function's argument types and return type (void)
c_find_eigenvalues.argtypes = [C_Matrix, C_EigenvaluesArray]
c_find_eigenvalues.restype = None

# --- Part 2: Solve the Problem Using the C Function ---

print("Following the method: find eigenvalues using C, then find their product.\n")

# Step 1: Define the matrix A in Python
A_py = np.array([
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
])
print("Step 1: Define the matrix A")
print(A_py)

# Convert the Python matrix to its C-compatible type
A_c = C_Matrix()
for i in range(SIZE):
    for j in range(SIZE):
        A_c[i][j] = A_py[i, j]

# Prepare the output array for the C function to write into
eigenvalues_result_c = (ctypes.c_double * SIZE)()

# Step 2: Call the C function to calculate the eigenvalues
c_find_eigenvalues(A_c, eigenvalues_result_c)

# Convert the C array result back into a Python list
eigenvalues = list(eigenvalues_result_c)

print("\nStep 2: Solve for eigenvalues (λ) using the C function")
print(f"The calculated eigenvalues are: {eigenvalues}")

# Step 3: Calculate the product of the found eigenvalues
product_of_eigenvalues = np.prod(eigenvalues)

print("\nStep 3: Calculate the product of the eigenvalues")
print(f"Product = {eigenvalues[0]} * {eigenvalues[1]} * {eigenvalues[2]}")
print(f"\nThe final product is: {product_of_eigenvalues}")
