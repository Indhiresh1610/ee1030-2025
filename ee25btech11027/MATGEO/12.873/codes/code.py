import ctypes
import platform
import math

# --- Python with C Library Solution ---

# Step 1: Load the C library.
lib_name = 'code.so' if platform.system() != 'Windows' else 'inner_product_lib.dll'
try:
    c_lib = ctypes.CDLL('./' + lib_name)
except OSError as e:
    print(f"Error: Could not load the C library '{lib_name}'.")
    print("Please make sure you have compiled the 'inner_product_lib.c' file first.")
    exit()

# Step 2: Define the function signature from the C library.
# The function name is 'calculate_inner_product'.
c_inner_product = c_lib.calculate_inner_product

# Define the C-compatible array type for a 3-element double array.
C_DoubleArray3 = ctypes.c_double * 3

# Specify the function's argument types and return type.
# It takes two pointers to double arrays and returns a double.
c_inner_product.argtypes = [C_DoubleArray3, C_DoubleArray3]
c_inner_product.restype = ctypes.c_double

# Step 3: Define the vectors in Python.
a_py = (math.sqrt(2), 1/math.sqrt(2), 1.0)
b_py = (1/math.sqrt(2), math.sqrt(2), -1.0)

# Convert Python tuples into the C-compatible array types.
a_c = C_DoubleArray3(*a_py)
b_c = C_DoubleArray3(*b_py)

print("Vectors being passed to C function:")
print(f"a = {list(a_c)}")
print(f"b = {list(b_c)}")

# Step 4: Call the C function with the vector data.
result = c_inner_product(a_c, b_c)

print(f"\nThe inner product calculated by the C function is: {result}")
