import threading
import time

def worker(name, count):
    """Function that will run in a separate thread."""
    for i in range(count):
        print(f"Worker {name}: iteration {i + 1}")
        time.sleep(0.5)  # Simulate work by pausing half a second

# Create a thread running the worker function.
thread1 = threading.Thread(target=worker, args=("A", 5))
thread2 = threading.Thread(target=worker, args=("B", 3))

# Start the threads.
thread1.start()
thread2.start()

# Wait for both threads to complete.
thread1.join()
thread2.join()

print("All threads have finished.")
