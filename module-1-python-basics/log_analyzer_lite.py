import re

def parse_log(file_path):
    failed_attempts = 0
    ip_addresses = set()
    users = set()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "Failed Password" in line:
                failed_attempts += 1

                parts = line.split()
                
                from_index = parts.index("from")
                ip = parts[from_index + 1]

                for_index = parts.index("for")

                if parts[for_index + 1] == "invalid":
                    user = parts[for_index + 3]
                else:
                    user = parts[for_index + 1]
                
                ip_addresses.add(ip)
                users.add(user)

    print("Log Analyzer Lite Summary")
    print("-------------------------")
    print(f"Total Failed Attempts: {failed_attempts}")
    print(f"IP Addresses: {', '.join(sorted(ip_addresses))}")
    print(f"Users: {', '.join(sorted(users))}")


parse_log("auth.log")