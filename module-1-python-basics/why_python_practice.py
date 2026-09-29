failed_logins = 7
username = "admin"

if failed_logins >= 5:
    print(f"Alert: {username} has suspicious login activity.")
else:
    print(f"{username} login activity appears normal.")