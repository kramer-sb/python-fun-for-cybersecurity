failed_logins = 0
username = "Admin"
if failed_logins >= 3:
    print(f"Review account: {username}")
    print(f"Reason: multiple failed longins")
else:
    print("No review needed.")
print("Script complete")

ports = [22, 80,443]
for port in ports:
    print (port)

username = "Admin"
if username == "Admin":
    print("Admin account")

def show_message():
    print("hello")
show_message()