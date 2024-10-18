import pyautogui as gui
import cv2
import numpy as np

import matplotlib.pyplot as plt

# Data
sieve_sizes = np.array([26.5, 19, 13.2, 4.75, 2, 0.425, 0.075])
percentage_passing = np.array([96.19, 48.6, 33.4, 16.4, 9.1, 3.4, 0])

# Create the plot
plt.figure(figsize=(10, 6))
plt.semilogx(sieve_sizes, percentage_passing, 'bo-')
plt.grid(True, which="both", ls="-", alpha=0.5)

# Set labels and title
plt.xlabel('Sieve Size (mm)')
plt.ylabel('Percentage Passing (%)')
plt.title('Sieve Analysis Graph')

# Set x-axis
plt.xlim(0.01, 100)
plt.xticks([0.1, 1, 10, 100], ['0.1', '1', '10', '100'])

# Set y-axis
plt.ylim(0, 100)

# Add data labels
for x, y in zip(sieve_sizes, percentage_passing):
    plt.annotate(f'{y:.1f}%', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Save the plot as a high-resolution PNG file
plt.savefig('sieve_analysis_graph.png', dpi=300, bbox_inches='tight')

print("Graph has been saved as 'sieve_analysis_graph.png'")
# gui.alert(text='MATCH FOUND', title='Match Found', button='OK')
