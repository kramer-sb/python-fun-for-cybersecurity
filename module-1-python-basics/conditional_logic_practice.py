'''
failed_logins = int(input("Enter failed login count: "))

if failed_logins == 0:
    print("All good.")
elif failed_logins <= 3:
    print("Suspicious activity detected")
else: 
    print("ALERT: Brute-force behavior detected.")
'''

severity_level = input("Enter severity level: ")

severity = severity_level.strip().lower()

if severity == "critical":
    print(f"{severity}: Escalate immediately.")
elif severity == "high":
    print(f"{severity}: Review today.")
elif severity == "medium":
    print(f"{severity}: Review this week.")
else:
    print(f"{severity}: Track normally.")