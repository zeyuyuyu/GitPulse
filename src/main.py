import os
import time
import sys
import psutil
import subprocess

def monitor_system():
    """Continuously monitor system resources and optimize performance."""
    while True:
        # Get current CPU and memory usage
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent
        
        # Check if resources are overloaded
        if cpu_percent > 80 or mem_percent > 80:
            # Optimize by scaling down non-critical processes
            print(f"System resources overloaded. CPU: {cpu_percent}%, Memory: {mem_percent}%")
            optimize_system()
        
        # Wait before checking again
        time.sleep(5)

def optimize_system():
    """Dynamically optimize system performance by scaling down non-critical processes."""
    # Get list of running processes
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    
    # Sort processes by CPU and memory usage
    processes = sorted(processes, key=lambda p: p.info['cpu_percent'] + p.info['memory_percent'], reverse=True)
    
    # Scale down non-critical processes
    for process in processes:
        if process.info['cpu_percent'] < 10 and process.info['memory_percent'] < 10:
            continue
        try:
            process.suspend()
            print(f"Suspended process: {process.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == "__main__":
    monitor_system()
