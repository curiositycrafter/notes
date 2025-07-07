import threading
import time

# Simulated priority: lower number = higher priority
tasks = [
    {"name": "LowPriority", "priority": 3},
    {"name": "MediumPriority", "priority": 2},
    {"name": "HighPriority", "priority": 1}
]

def worker(name, priority):
    time.sleep(priority)  # Simulate delay based on "priority"
    print(f"{name} thread with priority {priority} is running")

threads = []

# Sort tasks based on priority (lower = higher priority)
for task in sorted(tasks, key=lambda x: x["priority"]):
    t = threading.Thread(target=worker, args=(task["name"], task["priority"]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All priority-based threads finished.")
