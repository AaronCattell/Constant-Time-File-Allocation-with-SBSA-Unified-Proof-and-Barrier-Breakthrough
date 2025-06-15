# sbsa_full_demo.py
# Combined demonstration of SBSA theory, task manager use case, and benchmarking

import math
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# SBSA core mapping logic
# -----------------------
size_classes = ['1KB', '2KB', '4KB', '8KB', '16KB', '32KB', 'Low', 'Medium', 'High', 'Critical']
slots = {s: i for i, s in enumerate(size_classes)}

def map_file(size_class, thickness, width):
    slot = slots.get(size_class, -1)
    if slot == -1:
        raise ValueError("Invalid size class")
    return (slot, thickness, width)

def map_task(priority, layer, duration):
    if priority not in slots:
        raise ValueError("Invalid priority class")
    return (slots[priority], layer, duration)

# -----------------------
# Task manager use case
# -----------------------
def simulate_task_manager():
    tasks = [
        ('Low', 0, 0.5),
        ('Medium', 1, 1.0),
        ('High', 0, 2.0),
        ('Critical', 0, 4.5),
        ('Critical', 1, 1.5)
    ]
    print("\nTask Scheduling Map:")
    for t in tasks:
        print(f"Task {t} →", map_task(*t))

# -----------------------
# Benchmark SBSA vs log(n)
# -----------------------
class SBSA:
    def __init__(self, size_classes):
        self.slots = {s: [] for s in size_classes}

    def insert(self, size_class, file_id):
        self.slots[size_class].append(file_id)

class SimulatedLogN:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.data.sort()

def benchmark_sbsa(files):
    sbsa = SBSA(SIZE_CLASSES)
    for size, fid in files:
        sbsa.insert(size, fid)

def benchmark_logn(files):
    tree = SimulatedLogN()
    for _, fid in files:
        tree.insert(fid)

def run_benchmark(num_files=10000):
    files = [(random.choice(SIZE_CLASSES), f"file_{i}") for i in range(num_files)]
    sbsa_time = timeit.timeit(lambda: benchmark_sbsa(files), number=1)
    logn_time = timeit.timeit(lambda: benchmark_logn(files), number=1)
    print(f"SBSA Time: {sbsa_time:.4f}s")
    print(f"B-tree Time: {logn_time:.4f}s")
    print(f"Speedup: {logn_time / sbsa_time:.1f}x")

# -----------------------
# Chart SBSA vs log(n) growth
# -----------------------
def plot_growth_chart():
    n_values = np.logspace(1, 9, num=200)
    sbsa = n_values
    logn = n_values * np.log2(n_values)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, sbsa, label='SBSA (O(1))', color='green', linewidth=2)
    plt.plot(n_values, logn, label='B-tree / Skip List (O(log n))', color='blue', linewidth=2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of File Events (n)')
    plt.ylabel('Total Steps')
    plt.title('SBSA vs B-tree/Skip List Growth Rates')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig("sbsa_vs_logn_growth_chart.png")
    plt.show()

# -----------------------
# Run Demo
# -----------------------
if __name__ == '__main__':
    SIZE_CLASSES = ['1K', '2K', '4K', '8K', '16K', '32K']
    simulate_task_manager()
    run_benchmark(10000)
    plot_growth_chart()
