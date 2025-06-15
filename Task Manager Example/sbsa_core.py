# sbsa_core.py

# Define task priority classes
size_classes = ['Low', 'Medium', 'High', 'Critical']
slots = {s: i for i, s in enumerate(size_classes)}

def map_task(priority, layer, duration):
    """
    Map a task into a slot (by priority), with a layer and duration.
    Returns a tuple: (slot index, thickness layer, duration width)
    """
    if priority not in slots:
        raise ValueError("Invalid priority class")
    return (slots[priority], layer, duration)
