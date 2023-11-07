import subprocess
import json

def establish_internet_connection(config_path):
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    apn = config["sim_module"]["apn"]
    username = config["sim_module"]["username"]
    password = config["sim_module"]["password"]

    try:
        # Check if the modem is already connected
        status = subprocess.check_output("nmcli c show --active", shell=True).decode()
        if "modem" in status:
            print("Modem is already connected.")
            return

        # Create a new connection profile
        connection_name = "cellular"
        subprocess.call(f"nmcli c add con-name {connection_name} ifname '*' type gsm", shell=True)

        # Configure connection settings
        subprocess.call(f"nmcli c modify {connection_name} apn {apn} user {username} password {password}", shell=True)

        # Connect to the modem
        subprocess.call(f"nmcli c up {connection_name}", shell=True)

        print("Internet connection established successfully.")
    except Exception as e:
        print(f"Failed to establish an internet connection: {str(e)}")

