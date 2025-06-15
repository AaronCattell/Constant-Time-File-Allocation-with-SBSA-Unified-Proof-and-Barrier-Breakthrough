import matplotlib.pyplot as plt
import numpy as np

# Simulate n values from 10 to 10 million
n_values = np.logspace(1, 7, num=100)
sbsa = n_values
logn = n_values * np.log2(n_values)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, sbsa, label='SBSA (O(1))', color='green', linewidth=2)
plt.plot(n_values, logn, label='B-tree / Skip List (O(log n))', color='blue', linewidth=2)

# Formatting
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of File Events (n)', fontsize=12)
plt.ylabel('Total Steps', fontsize=12)
plt.title('SBSA vs B-tree/Skip List Growth Rates', fontsize=14)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save chart
plt.savefig("sbsa_vs_logn_growth_chart.png")
plt.show()
