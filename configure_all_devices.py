from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
import logging
import os  # For accessing environment variables

# Enable debug logging to help troubleshoot issues
logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)

# Get credentials securely from Jenkins environment
username = os.environ.get('CISCO_CREDS_USR')
password = os.environ.get('CISCO_CREDS_PSW')

# Confirm that credentials were passed in (optional safety check)
if not username or not password:
    raise ValueError("Missing credentials. Please ensure Jenkins provides CISCO_CREDS_USR and CISCO_CREDS_PSW.")

# Define your devices
devices = [
    {'ip': '10.10.10.2', 'hostname': 'reg-rtr'},
    {'ip': '10.10.10.3', 'hostname': 'ham-rtr'},
    {'ip': '10.10.10.4', 'hostname': 'mid-rtr'}
]

# Loop through and configure each device
for device in devices:
    try:
        print(f"\n[INFO] Connecting to {device['hostname']} at {device['ip']}...")

        # Establish SSH connection with credentials from environment
        conn = ConnectHandler(
            device_type='cisco_ios',
            ip=device['ip'],
            username=username,
            password=password,
            secret=password  # Assuming enable password = login password
        )
        conn.enable()  # Enter privileged exec mode

        # Define the commands to send
        commands = [
            f"hostname {device['hostname']}",
            "banner motd ^This device is managed by automation^"
        ]

        # Push the config
        output = conn.send_config_set(commands)
        print(f"[SUCCESS] Configured {device['hostname']}:\n{output}")

        # Save the config to startup-config
        save_output = conn.save_config()
        print(f"[INFO] Configuration saved on {device['hostname']}:\n{save_output}")

        # Disconnect when finished
        conn.disconnect()

    except NetmikoAuthenticationException:
        print(f"[ERROR] Authentication failed for {device['ip']} ({device['hostname']})")

    except NetmikoTimeoutException:
        print(f"[ERROR] Connection to {device['ip']} timed out")

    except Exception as e:
        print(f"[ERROR] Unexpected error with {device['ip']}: {str(e)}")
