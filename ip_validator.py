import re

def validate_ip_address(ip):
    # Regular expression for IPv4 address
    ip_regex = r'^(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$'
    ipv4_pattern = re.compile(ip_regex)

    return ipv4_pattern.match(ip) is not None

# Example usage
ip_address1 = "192.168.1.1"
ip_address2 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ip_address3 = "invalid_ip"

print(f"Is {ip_address1} a valid IP address? {validate_ip_address(ip_address1)}")
print(f"Is {ip_address2} a valid IP address? {validate_ip_address(ip_address2)}")
print(f"Is {ip_address3} a valid IP address? {validate_ip_address(ip_address3)}")
