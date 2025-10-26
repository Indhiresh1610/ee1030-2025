import numpy as np

# --- Native Python Solution ---
print("Following the method: find eigenvalues, then find their product.")

# Step 1: Define the matrix A from the question
A = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
])

print("\nStep 1: Define the matrix A")
print(A)

# Step 2: Find the eigenvalues of the matrix A
# This is equivalent to solving the characteristic equation |A - λI| = 0.
# We use NumPy's `linalg.eigvals()` to get the values of λ.
eigenvalues = np.linalg.eigvals(A)

# Round the values for clean display, as calculations can have small float errors.
rounded_eigenvalues = np.round(eigenvalues, decimals=5)
print("\nStep 2: Solve for the eigenvalues (λ)")
print(f"The calculated eigenvalues are: {rounded_eigenvalues}")

# Step 3: Calculate the product of the found eigenvalues
product_of_eigenvalues = np.prod(eigenvalues)

# Round the final product for a clean result.
final_product = np.round(product_of_eigenvalues)

print("\nStep 3: Calculate the product of the eigenvalues")
print(f"Product = {rounded_eigenvalues[0]} * {rounded_eigenvalues[1]} * {rounded_eigenvalues[2]}")
print(f"\nThe final product is: {final_product}")
