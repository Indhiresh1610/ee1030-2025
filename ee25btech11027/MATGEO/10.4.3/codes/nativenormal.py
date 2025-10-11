import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D # Needed for the custom legend

# --- 1. Define Point of Contact ---
contact_x = 2
contact_y = contact_x + 1/contact_x

print(f"--- Native Python Solution ---")
print(f"The point of contact is ({contact_x}, {contact_y})")

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

# Plot the complete hyperbola using a contour plot
plt.contour(X, Y, hyperbola_eq, levels=[0], colors='blue', linewidths=2)

# Plot the other geometric elements
plt.plot(plot_range, line, color='red', linestyle='--')
plt.plot(plot_range, normal_line, color='green')
plt.scatter(contact_x, contact_y, color='black', s=60, zorder=5) # Emphasize the point

# --- Create a custom legend for clarity ---
legend_elements = [
    Line2D([0], [0], color='blue', lw=2, label='Hyperbola: $x^2 - xy + 1 = 0$'),
    Line2D([0], [0], color='red', linestyle='--', label='Line: $3x - 4y - 7 = 0$'),
    Line2D([0], [0], color='green', label='Normal to Curve'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='k', markersize=8,
           label=f'Point of Contact ({contact_x}, {contact_y:.1f})')
]

# --- Formatting ---
plt.text(contact_x + 0.2, contact_y, f'({contact_x}, {contact_y:.1f})', fontsize=12)
plt.title('Figure')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend(handles=legend_elements)
plt.axis('equal') # Ensures perpendicular lines look perpendicular
plt.ylim(-6, 6)
plt.xlim(-6, 6)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/10.4.3/figs/figure1.png")
plt.show()
