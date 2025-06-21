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

✅ SBSA Async Queue shows near-linear or sublinear scaling

✅ SBSA LLM Memory Benchmarking

✅ SBSA Cube

✅ SBSA Cube agent memory Agent Memory for LLMs

✅ SBSA Cube Rule Engine

NEW 
🧊 SBSA Cube — Constant-Time Spatial Memory
SBSA Cube is the foundational logic layer of SBSA. It enables constant-time, multi-key storage by projecting each data point (e.g., task, memory, job) onto six mirrored file paths that form a virtual cube.

Instead of filtering lists or using tree-based lookups, SBSA Cube stores every payload using three orthogonal axes:



![e9ef87ae-6383-435b-8e31-3dc14db6af22](https://github.com/user-attachments/assets/32381409-5573-4dbb-aeab-133e308b95a8)
![Diagram](https://github.com/user-attachments/assets/17d9ea33-1cf6-4610-aa8d-53c7e2ef3de1)
![sbsa_vs_logn_growth_chart](https://github.com/user-attachments/assets/95c5145d-c6ac-40e0-ac22-ec32cd87b6cf)
![sbsa_vs_heap_benchmark](https://github.com/user-attachments/assets/34c2eb0d-b7a8-4260-a44b-e9ee281abb73)
![SBSA-Backed Quantum Job Queue With Qiskit](https://github.com/user-attachments/assets/04a3b85e-5379-4308-a441-8d2f24051925)
![sbsa_async_queue_benchmark](https://github.com/user-attachments/assets/54ef5bbf-187c-4ebc-8b69-afbf21eecb8c)
![sbsa_binary_queue VS JSON Queue Performance - Copy](https://github.com/user-attachments/assets/d6e4fe4e-b6cf-4b03-a212-61b6845bf89a)
![sbsa_llm_memory_benchmark](https://github.com/user-attachments/assets/80f1ed24-e97c-4966-94cb-775f510b252e)
![visual diagram of this architecture](https://github.com/user-attachments/assets/c64ada10-f08d-4cb6-bd17-42a7226e6031)
![sbsa_vs_cube_benchmark](https://github.com/user-attachments/assets/3b845e07-89a4-4d17-b621-f8814917ffd6)
![job_dispatch_benchmark png](https://github.com/user-attachments/assets/b5d1b177-d000-47bf-89a6-4a254fc350b3)
![sbsa_vs_flat_memory_benchmark](https://github.com/user-attachments/assets/5b4def03-5ef0-47b7-8c4e-f3df4ea53a05)
![SBSA Rule Cube vs a traditional flat list of rules](https://github.com/user-attachments/assets/17a02537-45f0-4b70-b1a8-27e745589dce)




📘 [Usage Guide →](USAGE.md)

https://youtu.be/8Y5VbyLC0GQ
https://youtu.be/gS9yDMRaYrQ
https://youtu.be/l2L_Lgm_jEA
