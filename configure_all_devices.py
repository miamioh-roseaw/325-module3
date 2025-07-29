from netmiko import ConnectHandler

devices = [
       {'ip': '10.10.10.2', 'hostname': 'reg-rtr'},
       {'ip': '10.10.10.3', 'hostname': 'ham-rtr'},
       {'ip': '10.10.10.4', 'hostname': 'mid-rtr'}
]

for device in devices:
       print(f"\n[INFO] Connecting to {device['hostname']} at {device['ip']}...")
       conn = ConnectHandler(
       device_type='cisco_ios',
       ip=device['ip'],
       username='student',
       password='Passw0rd!'
       )

       commands = [
       f"hostname {device['hostname']}",
       "banner motd ^This device is managed by automation^"
       ]

       output = conn.send_config_set(commands)
       print(f"[SUCCESS] Configured {device['hostname']}:\n{output}")
       conn.disconnect()
