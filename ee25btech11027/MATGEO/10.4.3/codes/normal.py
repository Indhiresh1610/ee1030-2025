import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D # Needed for custom legend

# --- 1. C Library Integration (No changes here) ---

try:
    solver_lib = ctypes.CDLL('./normal.so')
except OSError:
    print("Could not load 'libsolver.so'. Please compile solver.c first.")
    exit()

solve_func = solver_lib.solve_for_point
solve_func.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
solve_func.restype = None

line_A = ctypes.c_double(3.0)
line_B = ctypes.c_double(-4.0)
contact_x_ptr = ctypes.c_double()
contact_y_ptr = ctypes.c_double()

solve_func(line_A, line_B, ctypes.byref(contact_x_ptr), ctypes.byref(contact_y_ptr))

contact_x = contact_x_ptr.value
contact_y = contact_y_ptr.value

print("--- Python with C Library Solution ---")
print(f"The point of contact is ({contact_x:.1f}, {contact_y:.2f})")


# --- 2. Plotting (Modified Section) ---

# Define a wider range to see the full conic
plot_range = np.linspace(-6, 6, 500)
X, Y = np.meshgrid(plot_range, plot_range)

# Define the implicit equation of the hyperbola: x^2 - xy + 1 = 0
hyperbola_eq = X**2 - X*Y + 1

# The tangent and normal lines, plotted over the new wider range
line = (3*plot_range - 7) / 4
normal_line = (-4/3)*(plot_range - contact_x) + contact_y

# --- Create the Plot ---
plt.figure(figsize=(10, 10))

# Plot the complete hyperbola using a contour plot for the level where the equation is 0
plt.contour(X, Y, hyperbola_eq, levels=[0], colors='blue', linewidths=2)

# Plot the other geometric elements
plt.plot(plot_range, line, color='red', linestyle='--')
plt.plot(plot_range, normal_line, color='green')
plt.scatter(contact_x, contact_y, color='black', s=60, zorder=5) # Emphasize the point

# --- Create a custom legend because plt.contour doesn't auto-label ---
legend_elements = [
    Line2D([0], [0], color='blue', lw=2, label='Hyperbola: $x^2 - xy + 1 = 0$'),
    Line2D([0], [0], color='red', linestyle='--', label='Line: $3x - 4y - 7 = 0$'),
    Line2D([0], [0], color='green', label='Normal to Curve'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='k', markersize=8,
           label=f'Point of Contact ({contact_x:.1f}, {contact_y:.2f})')
]
plt.text(contact_x + 0.2, contact_y, f'({contact_x}, {contact_y:.1f})', fontsize=12)
plt.title('Figure')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend(handles=legend_elements)
plt.axis('equal')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/10.4.3/figs/figure1.png")
plt.show()
