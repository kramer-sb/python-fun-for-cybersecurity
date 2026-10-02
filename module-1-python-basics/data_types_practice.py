username = "cyber_student"
failed_attempts = 3
is_logged_in = False
ip_addresses = ["192.168.1.10", "10.0.0.5"]
finding = {
    "title": "Multiple failed logins",
    "severity": "medium", 
    "status": "open"
}
print(f"Username: {username}")
print(f"Failed attempts: {failed_attempts}")
print(f"Logged in? {is_logged_in}")
print(f"IP Addresses: {ip_addresses}")
print(f"Finding: {finding['title']} ({finding['severity']})")
print("---------------------------------------------------")
username = "admin"
source_ip = "192.168.1.25"
failed_logins = 5
threshold = 3
is_suspicious = failed_logins >= threshold
print(f"User {username} from {source_ip} had {failed_logins} failed attempts.")
print(f"Suspicious? {is_suspicious}")
print("----------------------------------------------------")

Username = "Power_User"
source_ip = "192.168.2.10"
failed_attempts = 4
threshold = 2
is_suspicious = failed_attempts >= threshold
print(f"User {username} from {source_ip} had {failed_attempts} failed attempts. Suspicious? {is_suspicious}.")
print("----------------------------------------------------")

