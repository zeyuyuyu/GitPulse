import os
import time

def main():
    """Main entry point of the application."""
    # Check if the device is running on battery power
    if is_on_battery():
        # Enable power-saving mode
        enable_power_saving_mode()
    else:
        # Run the application in normal mode
        run_normal_mode()

def is_on_battery():
    """Checks if the device is running on battery power."""
    # Implement platform-specific logic to check battery status
    if os.name == 'nt':
        # Windows implementation
        import win32api, win32power
        status = win32api.GetSystemPowerStatus()
        return status.BatteryFlag != 0
    elif os.name == 'posix':
        # Unix-like implementation
        with open('/sys/class/power_supply/BAT0/status', 'r') as f:
            status = f.read().strip()
        return status == 'Discharging'
    else:
        # Fallback to always return False
        return False

def enable_power_saving_mode():
    """Enables power-saving mode for the application."""
    # Implement power-saving logic, such as:
    # - Reducing screen brightness
    # - Disabling unused hardware components
    # - Optimizing CPU and memory usage
    print('Entering power-saving mode...')
    # Reduce screen brightness by 50%
    set_screen_brightness(50)
    # Disable Wi-Fi and Bluetooth
    disable_wireless_radios()
    # Optimize CPU and memory usage
    tune_system_performance()

def run_normal_mode():
    """Runs the application in normal mode."""
    # Implement the normal mode logic, such as:
    # - Restoring default settings
    # - Enabling all hardware components
    # - Running the main application functionality
    print('Running in normal mode...')
    # Restore screen brightness to 100%
    set_screen_brightness(100)
    # Enable Wi-Fi and Bluetooth
    enable_wireless_radios()
    # Run the main application functionality
    execute_main_functionality()

# Helper functions
def set_screen_brightness(brightness):
    """Sets the screen brightness to the specified level."""
    # Implement platform-specific logic to set the screen brightness
    pass

def disable_wireless_radios():
    """Disables the Wi-Fi and Bluetooth radios."""
    # Implement platform-specific logic to disable wireless radios
    pass

def enable_wireless_radios():
    """Enables the Wi-Fi and Bluetooth radios."""
    # Implement platform-specific logic to enable wireless radios
    pass

def tune_system_performance():
    """Optimizes CPU and memory usage for the application."""
    # Implement logic to optimize system performance
    pass

def execute_main_functionality():
    """Executes the main functionality of the application."""
    # Implement the main application logic
    pass

if __name__ == '__main__':
    main()