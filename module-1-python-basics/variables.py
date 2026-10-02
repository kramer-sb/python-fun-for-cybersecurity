#-----------------------------
# 1 NoneType
#-----------------------------

print("\n=== 1. NoneType: Represents No Value ===")

scan_result = None

print("Value:", scan_result)
print("Type:", type(scan_result))
print("Is the value None?", scan_result is None)

#-----------------------------
# 2 Integer
#-----------------------------

print("\n=== 2. int: Whole Numbers ===")
failed_logins = 3
maximum_attempts = 5

print("failed_logins =", failed_logins)
print("Type:", type(failed_logins))
print("After one more failed login:", failed_logins + 1)
print("Attempts remainding:", maximum_attempts - failed_logins)

# ---------------------------------------------------------------------------
# 3. FLOAT
# ---------------------------------------------------------------------------

print("\n=== 3. float: Decimal Numbers ===")

risk_score = 82.5
cpu_usage = 47.25
 
print("risk_score =", risk_score)
print("Type:", type(risk_score))
print("Risk as a percentage:", risk_score / 100)
print("Updated CPU usage:", cpu_usage + 5.5)

# ---------------------------------------------------------------------------
# 4. COMPLEX NUMBER
# ---------------------------------------------------------------------------

print("\n=== 4. complex: Real and Imaginary Numbers ===")

signal_value = 3 + 4j

print("signal_value =", signal_value)
print("Type:", type(signal_value))
print("Real portion:", signal_value.real)
print("Imaginary portion:", signal_value.imag)

# ---------------------------------------------------------------------------
# 5. BOOLEAN
# ---------------------------------------------------------------------------

print("\n=== 5. bool: True or False ===")

account_locked = False
mfa_enabled = True

print("account_locked =", account_locked)
print("Type:", type(account_locked))
print("mfa_enabled =", mfa_enabled)
print("Type:", type(mfa_enabled))

# Comparisons also produce Boolean values.
too_many_attempts = failed_logins >= maximum_attempts

print("Too many login attempts?", too_many_attempts)
print("Type:", type(too_many_attempts))


# ---------------------------------------------------------------------------
# 6. STRING
# ---------------------------------------------------------------------------

print("\n=== 6. str: Text ===")

username = "cyber_student"
username2 = str(10)
alert_message = "Suspicious login detected"

print("username =", username)
print("Type:", type(username))
print("Type:", type(username2))
print("Number of characters:", len(username))
print("Uppercase:", username.upper())
print("First character:", username[0])

# An f-string combines text and variables.
formatted_alert = f"Alert for {username}: {alert_message}"
print("Hi my name is " + username)
print(formatted_alert)


# ---------------------------------------------------------------------------
# 7. RANGE
# ---------------------------------------------------------------------------

print("\n=== 7. range: Sequence of Integers ===")

port_range = range(20, 26)

print("port_range =", port_range)
print("Type:", type(port_range))
print("Converted to a list:", list(port_range))

print("Looping through the range:")

for port in port_range:
    print("Checking port:", port)


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------

print("\n=== Summary ===")

print("NoneType | Represents no value")
print("int      | Whole numbers")
print("float    | Decimal numbers")
print("complex  | Real and imaginary numbers")
print("bool     | True or False")
print("str      | Text")
print("range    | Sequence of integers")