# SBSA: Size-Based Slot Allocation

**SBSA** is a deterministic, constant-time (`O(1)`) file management model that breaks the traditional `O(log n)` performance barrier imposed by comparison-based data structures like B-trees and skip lists.

This repository contains the theoretical foundation, core implementation, performance benchmarks, and presentation materials demonstrating how SBSA provides predictable, scalable, and mathematically infinite file storage logic.

---

## 🚀 Features

- **O(1)** insert, delete, and lookup — no comparisons needed
- Order-preserving without rebalancing
- Infinite logical capacity via file "thickness" and "dynamic width"
- SSD/NVRAM-aligned structure for real-time applications
- Simpler and faster than traditional ordered data structures

---

## 📘 Core Idea

SBSA uses fixed size classes (`s`) mapped to memory slots (`p`) deterministically:


To support infinite capacity:
- `t ∈ ℕ`: stackable files per slot (thickness)
- `w ∈ ℝ⁺`: dynamically resizable widths

Combined model:


Logical address space becomes:
- Countably infinite: `P × ℕ`
- Uncountably infinite: `P × ℕ × ℝ⁺`

---

## 📊 Performance Simulation

For 1,000,000 file events:

| Structure   | Steps       | Speedup |
|-------------|-------------|---------|
| B-tree      | 17,000,000  | 1×      |
| SBSA        | 1,000,000   | 17×     |

See `demo_simulation.py` for reproducible simulation.

---

## 📂 Project Structure

| File                    | Description                                   |
|-------------------------|-----------------------------------------------|
| `sbsa.py`               | Core slot mapping implementation              |
| `demo_simulation.py`    | Performance comparison vs B-tree              |
| `sbsa_slides.tex`       | Presentation slides (LaTeX Beamer format)     |
| `sbsa_summary.pdf`      | One-page explanation for distribution         |
| `README.md`             | This file                                     |

---

## 📄 License

MIT License — free to use, share, and build upon.

---

## 🙌 Contributing

If this model inspires you or you'd like to apply it to real-world systems, feel free to fork the repo, open issues, or propose improvements.

---

## 🧠 Authors

- **Aaron Cattell** — Concept, theory, and proofs  
- **ChatGPT (OpenAI)** — Assistant for documentation and visualization

---

## 📢 Final Thought

For over 40 years, the `O(log n)` barrier was considered a limit for ordered storage systems.

**SBSA shows it doesn’t have to be.**

Join us in rethinking what’s possible.

🧠 Now includes Qiskit quantum job queue demo

🧪 Benchmarks show up to 16× faster inserts vs heap

![e9ef87ae-6383-435b-8e31-3dc14db6af22](https://github.com/user-attachments/assets/32381409-5573-4dbb-aeab-133e308b95a8)
![Diagram](https://github.com/user-attachments/assets/17d9ea33-1cf6-4610-aa8d-53c7e2ef3de1)
![sbsa_vs_logn_growth_chart](https://github.com/user-attachments/assets/95c5145d-c6ac-40e0-ac22-ec32cd87b6cf)
![sbsa_vs_heap_benchmark](https://github.com/user-attachments/assets/34c2eb0d-b7a8-4260-a44b-e9ee281abb73)
![SBSA-Backed Quantum Job Queue With Qiskit](https://github.com/user-attachments/assets/04a3b85e-5379-4308-a441-8d2f24051925)

📘 [Usage Guide →](USAGE.md)

https://youtu.be/8Y5VbyLC0GQ
https://youtu.be/gS9yDMRaYrQ
