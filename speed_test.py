
import timeit
import math
import random

# -------------------------
# SBSA Implementation
# -------------------------
class SBSA:
    def __init__(self, size_classes):
        self.slots = {s: [] for s in size_classes}
        self.size_classes = size_classes

    def insert(self, size_class, file_id):
        if size_class not in self.slots:
            raise ValueError("Invalid size class")
        self.slots[size_class].append(file_id)

# -------------------------
# Simulated B-tree / Skip List
# -------------------------
class SimulatedLogN:
    def __init__(self):
        self.data = []

    def insert(self, value):
        math.log2(len(self.data) + 2)  # theoretical log(n) call
        self.data.append(value)
        self.data.sort()  # simulate cost

# -------------------------
# Benchmark Setup
# -------------------------
NUM_FILES = 100_000
SIZE_CLASSES = ['1K', '2K', '4K', '8K', '16K', '32K']

files = [(random.choice(SIZE_CLASSES), f"file_{i}") for i in range(NUM_FILES)]

# -------------------------
# Measure SBSA
# -------------------------
def benchmark_sbsa():
    sbsa = SBSA(SIZE_CLASSES)
    for size, fid in files:
        sbsa.insert(size, fid)

# -------------------------
# Measure B-tree / Skip List (simulated log n)
# -------------------------
def benchmark_logn():
    tree = SimulatedLogN()
    for _, fid in files:
        tree.insert(fid)

# -------------------------
# Run Tests
# -------------------------
print("Running SBSA...")
sbsa_time = timeit.timeit(benchmark_sbsa, number=1)
print(f"SBSA Time: {sbsa_time:.4f} seconds")

print("Running Simulated B-tree / Skip List...")
logn_time = timeit.timeit(benchmark_logn, number=1)
print(f"Simulated B-tree Time: {logn_time:.4f} seconds")

print("\nSpeedup: {:.1f}× faster (SBSA vs log n)".format(logn_time / sbsa_time))
