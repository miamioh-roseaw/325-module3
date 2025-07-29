from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
import logging

logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)

devices = [
    {'ip': '10.10.10.2', 'hostname': 'reg-rtr'},
    {'ip': '10.10.10.3', 'hostname': 'ham-rtr'},
    {'ip': '10.10.10.4', 'hostname': 'mid-rtr'}
]

for device in devices:
    try:
        print(f"\n[INFO] Connecting to {device['hostname']} at {device['ip']}...")
        conn = ConnectHandler(
            device_type='cisco_ios',
            ip=device['ip'],
            username='student',
            password='Passw0rd!',
            secret='Passw0rd!'
        )
        conn.enable()

        commands = [
            f"hostname {device['hostname']}",
            "banner motd ^This device is managed by automation^"
        ]

        output = conn.send_config_set(commands)
        print(f"[SUCCESS] Configured {device['hostname']}:\n{output}")
        conn.disconnect()

    except NetmikoAuthenticationException:
        print(f"[ERROR] Authentication failed for {device['ip']} ({device['hostname']})")

    except NetmikoTimeoutException:
        print(f"[ERROR] Connection to {device['ip']} timed out")

    except Exception as e:
        print(f"[ERROR] Unexpected error with {device['ip']}: {str(e)}")
