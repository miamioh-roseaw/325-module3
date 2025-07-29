# Import necessary classes and exceptions from Netmiko
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
import logging  # Used for logging detailed connection/debug info to a file

# Enable Netmiko's debug logging and write it to 'netmiko.log'
# This is helpful for troubleshooting connection or command issues
logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)

# Define a list of network devices you want to connect to
# Each device includes an IP address and a desired hostname
devices = [
    {'ip': '10.10.10.2', 'hostname': 'reg-rtr'},
    {'ip': '10.10.10.3', 'hostname': 'ham-rtr'},
    {'ip': '10.10.10.4', 'hostname': 'mid-rtr'}
]

# Loop through each device in the list
for device in devices:
    try:
        # Print a message indicating which device is being connected to
        print(f"\n[INFO] Connecting to {device['hostname']} at {device['ip']}...")

        # Create an SSH connection to the Cisco device
        conn = ConnectHandler(
            device_type='cisco_ios',      # Device type tells Netmiko how to handle command syntax
            ip=device['ip'],              # The IP address of the device
            username='student',           # Username for SSH login
            password='Passw0rd!',         # Password for SSH login
            secret='Passw0rd!'            # Enable password for privileged exec mode
        )

        # Enter enable (privileged exec) mode
        conn.enable()

        # Define a list of configuration commands to send to the device
        commands = [
            f"hostname {device['hostname']}",                       # Set the hostname
            "banner motd ^This device is managed by automation^"    # Set the login banner message
        ]

        # Send the configuration commands to the device
        output = conn.send_config_set(commands)

        # Print the device response after sending the commands
        print(f"[SUCCESS] Configured {device['hostname']}:\n{output}")

        # Save the configuration so changes persist after reboot
        # Equivalent to typing 'write memory' on the router
        save_output = conn.save_config()
        print(f"[INFO] Configuration saved on {device['hostname']}:\n{save_output}")

        # Disconnect from the device after we're done
        conn.disconnect()

    # If login credentials are wrong, this block will run
    except NetmikoAuthenticationException:
        print(f"[ERROR] Authentication failed for {device['ip']} ({device['hostname']})")

    # If the device is offline or the IP is wrong, this block will run
    except NetmikoTimeoutException:
        print(f"[ERROR] Connection to {device['ip']} timed out")

    # Catch any other unexpected errors (such as command typos, network failures, etc.)
    except Exception as e:
        print(f"[ERROR] Unexpected error with {device['ip']}: {str(e)}")
