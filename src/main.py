import os
import time
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

def monitor_system_metrics():
    """Continuously monitor system metrics and send alerts for critical thresholds."""
    while True:
        cpu_usage = get_cpu_usage()
        mem_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        
        if cpu_usage > 90:
            send_alert(f"CPU usage critical at {cpu_usage}%")
        if mem_usage > 85:
            send_alert(f"Memory usage critical at {mem_usage}%")
        if disk_usage > 90:
            send_alert(f"Disk usage critical at {disk_usage}%")
        
        time.sleep(60)  # Check metrics every minute

def get_cpu_usage():
    """Get the current CPU usage percentage."""
    output = subprocess.check_output(['top', '-bn1', '|', 'grep', 'Cpu(s)'])
    cpu_usage = float(output.decode().split(',')[0].split()[1])
    return cpu_usage

def get_memory_usage():
    """Get the current memory usage percentage."""
    output = subprocess.check_output(['free'])
    mem_total = float(output.decode().split()[7])
    mem_used = float(output.decode().split()[8])
    mem_usage = (mem_used / mem_total) * 100
    return mem_usage

def get_disk_usage():
    """Get the current disk usage percentage."""
    disk_usage = shutil.disk_usage("/").percent
    return disk_usage

def send_alert(message):
    """Send an alert notification for a critical system metric."""
    logging.warning(message)
    # Add integration with a monitoring/alerting service here

if __name__ == "__main__":
    monitor_system_metrics()
