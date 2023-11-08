
import subprocess
import json

def establish_internet_connection(config_path):
    try:
        # Read configuration from config.json
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        
        # Get APN and USB interface from the configuration
        apn = config.get("sim_apn", "YOUR_DEFAULT_APN")
        usb_interface = config.get("sim_usb_interface", "YOUR_DEFAULT_USB_INTERFACE")

        # Run the sakis3g command to establish the internet connection
        result = subprocess.run(["sudo", "sakis3g", "connect", f"APN={apn}", f"USBINTERFACE={usb_interface}"], capture_output=True, text=True, check=True)

        # Check if the connection was successful
        if result.returncode == 0:
            print("Internet connection established successfully.")
            print(result.stdout)  
        else:
            print("Failed to establish the internet connection.")
            print(result.stderr)  

    except Exception as e:
        print(f"An error occurred: {str(e)}")
