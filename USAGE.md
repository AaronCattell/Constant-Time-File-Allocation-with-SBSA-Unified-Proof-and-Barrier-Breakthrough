# 📘 SBSA — Usage Guide

This guide shows how to install, run, and apply SBSA (Size-Based Slot Allocation), a constant-time file and task classification model that breaks the `O(log n)` barrier.

---

## 📦 Installation

### ✅ Requirements

- Python 3.7+
- `matplotlib` and `numpy` (for charting)

Install dependencies:
```bash
pip install matplotlib numpy
```

Clone the repository:
```bash
git clone https://github.com/yourusername/sbsa
cd sbsa
```

---

## ▶️ Basic Usage

Run the combined demo:
```bash
python sbsa_full_demo.py
```

This will:
- Show how SBSA maps priority tasks
- Run a benchmark vs simulated B-tree
- Generate a growth chart (`sbsa_vs_logn_growth_chart.png`)

---

## 🔁 Reusable Function

You can import and use SBSA in your own project:

```python
from sbsa_core import map_file

map_file('4KB', 2, 3.5)  # → (slot_id, thickness_layer, width)
```

Or for a task scheduler:

```python
from sbsa_core import map_task

map_task('High', 0, 1.5)  # → (priority_slot, layer, duration)
```

---

## 📂 Examples

See `/examples` folder for:
- `example_basic_insert.py`
- `example_thickness.py`
- `example_dynamic_width.py`
- `example_invalid_class.py`

Each one runs independently:
```bash
python examples/example_thickness.py
```

---

## 📊 Benchmarking

Run:
```bash
python speed_test.py
```

This will compare SBSA insertions to a simulated B-tree:
- Inserts 100,000 files
- Prints timing and speedup

---

## 📈 Chart SBSA vs Log(n)

Generate a growth rate comparison up to 1 billion events:
```bash
python sbsa_vs_logn_chart.py
```

Output:
- `sbsa_vs_logn_growth_chart.png`

---

## 💡 Use Cases

- Replacing B-tree for real-time logs, indexes, task queues
- Priority schedulers (e.g. OS, to-do apps)
- File systems with deterministic layout
- Data models with infinite logical layering

---

## 🤝 Contributing

Found a use case or optimization?  
Check the [CONTRIBUTING.md](CONTRIBUTING.md) or open a discussion!

---

## 🧠 Theory

For a deep dive:
- See `sbsa_slides.tex`
- Read `sbsa_summary.pdf`
- Browse the `/docs` folder

---

## 🔗 Credits

Created by **Aaron Cattell** with support from ChatGPT (OpenAI).  
Inspired by the question: *“Can we break the `O(log n)` wall?”*

---

## 🔒 License

MIT — free to use, share, and build on.
