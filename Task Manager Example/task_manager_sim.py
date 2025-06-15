# task_manager_sim.py

from sbsa_core import map_task

# Simulated task queue
tasks = [
    ('Low', 0, 0.5),
    ('Medium', 1, 1.0),
    ('High', 0, 2.0),
    ('Critical', 0, 4.5),
    ('Critical', 1, 1.5)
]

print("Task Scheduling Map:")
for t in tasks:
    print(f"Task {t} →", map_task(*t))
