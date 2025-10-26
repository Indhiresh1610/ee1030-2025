import numpy as np

# --- Native Python Solution ---
print("Method: Represent vectors as arrays and compute the inner product (a.b).")

# Step 1: Define the vectors a and b as NumPy arrays.
# These correspond to the column matrices in the image.
a = np.array([np.sqrt(2), 1/np.sqrt(2), 1])
b = np.array([1/np.sqrt(2), np.sqrt(2), -1])

print("\nVector a:")
print(a)
print("\nVector b:")
print(b)

# Step 2: Calculate the inner product using np.dot() or the @ operator.
# This is equivalent to a^T * b in matrix notation.
inner_product = a @ b
# Alternatively: inner_product = np.dot(a, b)

print(f"\nCalculation: a.b = ({a[0]:.3f} * {b[0]:.3f}) + ({a[1]:.3f} * {b[1]:.3f}) + ({a[2]:.3f} * {b[2]:.3f})")
print(f"               = {a[0]*b[0]} + {a[1]*b[1]} + {a[2]*b[2]}")


print(f"\nThe inner product (a.b) is: {inner_product}")
