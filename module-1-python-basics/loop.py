"""
Python Loops and Lists
Walkthrough for Visual Studio Code and AREPL

Change EXAMPLE_NUMBER to select the example shown in the AREPL output.

 1  Creating lists
 2  List indexes and slicing
 3  Common list operations
 4  Basic for loop
 5  Looping through a cybersecurity port list
 6  Using range()
 7  Basic while loop
 8  Filtering alerts into a new list
 9  Filtering web ports
10  List comprehension preview
11  Splitting a string into a list
12  Looping through dictionaries in a list
13  Simulating loops through file lines
14  Port-classification practice
15  Privileged-account challenge
16  Combined cybersecurity example

AREPL NOTE 
----------
These examples use editable variables instead of input() so AREPL can
rerun the file immediately. Examples that read an actual file are
included near the bottom as commented terminal-ready code.
"""

# Change this number to change Example:
EXAMPLE_NUMBER = 3
 
# %% 1. CREATING LISTS

if EXAMPLE_NUMBER == 1:
    print("\n=== 1. Creating Lists ===")

    # A list stores multiple values in one variable.
    # Don't normally have different types in a list.
    ports = [22, 80, 443, 3389]
    Newlist = []
    tools = ["nmap", "curl", "whois",int(123)]

    # A list can also contain dictionaries.
    
    findings = [
        {"title": "Weak password policy", "severity": "medium"},
        {"title": "Missing patch", "severity": "high"},
    ]

    print("Port list:", ports)
    print("Tool list:", tools)
    print("Finding list:", findings)

    print("\nData types:")
    print("type(ports):", type(ports))
    print("type(ports[0]):", type(ports[0]))
    print("type(tools[0]):", type(tools[0]))
    print("type(findings[0]):", type(findings[0]))
    print("type(tools[3]):", type(tools[3]))

# %% 2. LIST INDEXES AND SLICING

if EXAMPLE_NUMBER == 2:
    print("\n=== 2. List Indexes and Slicing ===")

    ports = [22, 80, 443, 3389]

    print("Entire list:", ports)
    print("ports[0]:", ports[0])
    print("ports[1]:", ports[1])
    print("ports[2]:", ports[2])
    print("ports[3]:", ports[3])

    # Negative indexes count backward from the end.
    print("\nLast item with ports[-1]:", ports[-1])

    # A slice returns part of a list.
    print("First two items with ports[0:2]:", ports[0:2])
    print("Items from index 1 onward:", ports[1:])

    # List indexes begin at 0.
    #
    # The following would cause an IndexError:
    # print(ports[10])
    # Change one of the indexes, what's the result?.


# %% 3. COMMON LIST OPERATIONS

if EXAMPLE_NUMBER == 3:
    print("\n=== 3. Common List Operations ===")

    tools = ["nmap", "curl", "whois"]

    print("Starting list:", tools)

    # append() adds one item to the end.
    tools.append("dig")
    print("After append():", tools)

    # The in operator checks whether a value exists.
    print('Is "nmap" in tools?', "nmap" in tools)
    print('Is "nikto" in tools?', "nikto" in tools)

    # len() counts the number of items.
    print("Number of tools:", len(tools))

    # Lists are mutable, so an item can be changed.
    tools[1] = "wget"
    print("After changing index 1:", tools)

    # remove() removes the first matching value.
    tools.remove("whois")
    print('After remove("whois"):', tools)



# %% 4. BASIC FOR LOOP

if EXAMPLE_NUMBER == 4:
    print("\n=== 4. Basic for Loop ===")

    ports = [22, 80, 443]

    print("Ports:", ports)
    print()

    # The loop runs once for each item in the list.
    for port in ports:
        print(f"Checking port {port}")

    print("\nThe loop has finished.")

    # During each repetition, port temporarily holds one list item.
    #
    # First repetition:  port = 22
    # Second repetition: port = 80
    # Third repetition:  port = 443


# %% 5. CYBERSECURITY PORT LIST

if EXAMPLE_NUMBER == 5:
    print("\n=== 5. Cybersecurity Example: Port List ===")

    common_ports = [22, 80, 443, 3389]

    for port in common_ports:
        print(f"Port {port} is commonly reviewed during assessments")

    # This example is not scanning a system.
    # It demonstrates processing stored port numbers one at a time.


# %% 6. USING RANGE()

if EXAMPLE_NUMBER == 6:
    print("\n=== 6. Using range() ===")

    print("range(5):")

    # range(5) starts at 0 and stops before 5.
    for number in range(5):
        print(number)

    print("\nrange(20, 26):")

    # The starting value is included.
    # The ending value is not included.
    for port in range(20, 26):
        print(f"Checking port {port}")

    print("\nrange(10, 0, -2):")

    # The third argument controls the step.
    for number in range(10, 0, -2):
        print(number)


# %% 7. BASIC WHILE LOOP

if EXAMPLE_NUMBER == 7:
    print("\n=== 7. Basic while Loop ===")

    attempt = 0
    maximum_attempts = 3

    # The loop continues while this condition is True.
    while attempt < maximum_attempts:
        print(f"Trying again, attempt {attempt + 1}")
        attempt += 1

    print("Maximum number of attempts reached.")
    print("Final value of attempt:", attempt)

    # attempt += 1 is the same as:
    # attempt = attempt + 1
    #
    # Without that update, attempt would remain 0 and the loop
    # would continue forever.
    # Change maximum_attempts to 5.


# %% 8. FILTERING ALERTS

if EXAMPLE_NUMBER == 8:
    print("\n=== 8. Filtering Alerts into a New List ===")

    alerts = [
        "Failed Login",
        "Unauthorized Access",
        "Firewall Block",
        "Successful Login",
    ]

    login_alerts = []

    print("All alerts:", alerts)
    print()

    for alert in alerts:
        print(f"Reviewing: {alert}")

        if "Login" in alert:
            print("  Match found")
            login_alerts.append(alert)
        else:
            print("  Not a login alert")

    print("\nFiltered login alerts:", login_alerts)

    # Pattern:
    # Start with many items
    # Loop through each item
    # Test a condition
    # Store matching items in a new list


# %% 9. FILTERING WEB PORTS

if EXAMPLE_NUMBER == 9:
    print("\n=== 9. Filtering Web Ports ===")

    ports = [21, 22, 80, 443, 3389]
    web_ports = []

    for port in ports:
        if port == 80 or port == 443:
            web_ports.append(port)
            print(f"Added web port: {port}")
        else:
            print(f"Skipped non-web port: {port}")

    print("\nOriginal ports:", ports)
    print("Web ports:", web_ports)

    # Add 8080 to the list and decide whether the condition should include it.


# %% 10. LIST COMPREHENSION PREVIEW

if EXAMPLE_NUMBER == 10:
    print("\n=== 10. List Comprehension Preview ===")

    ports = [21, 22, 80, 443, 3389]

    # Regular loop version.
    web_ports_loop = []

    for port in ports:
        if port == 80 or port == 443:
            web_ports_loop.append(port)

    # List comprehension version.
    web_ports_comprehension = [
        port
        for port in ports
        if port == 80 or port == 443
    ]

    print("Regular loop result:", web_ports_loop)
    print("List comprehension result:", web_ports_comprehension)
    print("Do both produce the same result?",
          web_ports_loop == web_ports_comprehension)

    # Read the comprehension from left to right:
    #
    # Add port
    # for each port in ports
    # if port is 80 or 443
    #
    # Regular loops are often easier to understand when first learning.


# %% 11. SPLITTING A STRING INTO A LIST

if EXAMPLE_NUMBER == 11:
    print("\n=== 11. Splitting a String into a List ===")

    log_line = "Failed password for admin from 192.168.1.20"

    print("Original string:")
    print(log_line)
    print("Type:", type(log_line))

    # split() separates the string at spaces and returns a list.
    parts = log_line.split()

    print("\nAfter split():")
    print(parts)
    print("Type:", type(parts))

    print("\nLooping through each word:")

    for part in parts:
        print(part)

    print("\nSelected values by index:")
    print("Event word:", parts[0])
    print("Username:", parts[3])
    print("IP address:", parts[5])


# %% 12. LIST OF DICTIONARIES

if EXAMPLE_NUMBER == 12:
    print("\n=== 12. Looping Through Dictionaries in a List ===")

    findings = [
        {
            "title": "Weak password policy",
            "severity": "medium",
        },
        {
            "title": "Missing security patch",
            "severity": "high",
        },
        {
            "title": "Default administrator password",
            "severity": "critical",
        },
    ]

    for finding in findings:
        title = finding["title"]
        severity = finding["severity"]

        print(f"{severity.upper()}: {title}")

    print("\nHigh-priority findings:")

    for finding in findings:
        if finding["severity"] == "high" or finding["severity"] == "critical":
            print(f'- {finding["title"]}')

    # Each loop item is one dictionary.
    # Dictionary keys provide access to the finding's fields.


# %% 13. SIMULATING FILE LINES

if EXAMPLE_NUMBER == 13:
    print("\n=== 13. Simulating a Loop Through File Lines ===")

    # These strings simulate lines read from an authentication log.
    log_lines = [
        "Accepted password for alice from 192.168.1.10\n",
        "Failed password for admin from 192.168.1.20\n",
        "Connection closed by 192.168.1.15\n",
        "Failed password for root from 192.168.1.30\n",
    ]

    failed_lines = []

    for line in log_lines:
        if "Failed password" in line:
            clean_line = line.strip()
            failed_lines.append(clean_line)
            print(clean_line)

    print("\nNumber of failed-password lines:", len(failed_lines))

    # strip() removes the newline character at the end of each line.
    #
    # An actual file-reading version is included at the bottom
    # of this walkthrough as commented code.


# %% 14. PORT-CLASSIFICATION PRACTICE

if EXAMPLE_NUMBER == 14:
    print("\n=== 14. Port-Classification Practice ===")

    ports = [22, 80, 443, 3389]

    for port in ports:
        if port == 22:
            print("SSH found")
        elif port == 80:
            print("HTTP found")
        elif port == 443:
            print("HTTPS found")
        else:
            print(f"Other port: {port}")

    # This combines:
    # - A list
    # - A for loop
    # - Conditional logic
    # - An f-string


# %% 15. PRIVILEGED-ACCOUNT CHALLENGE

if EXAMPLE_NUMBER == 15:
    print("\n=== 15. Privileged-Account Challenge ===")

    users = ["admin", "alice", "bob", "root", "guest"]

    for user in users:
        if user == "admin" or user == "root":
            print(f"{user}: Privileged account found")
        else:
            print(f"{user}: Standard account")


# %% 16. COMBINED CYBERSECURITY EXAMPLE

if EXAMPLE_NUMBER == 16:
    print("\n=== 16. Combined Cybersecurity Example ===")

    alerts = [
        {
            "message": "Successful login",
            "severity": "informational",
            "user": "alice",
        },
        {
            "message": "Repeated failed logins",
            "severity": "high",
            "user": "admin",
        },
        {
            "message": "Malware signature detected",
            "severity": "critical",
            "user": "bob",
        },
        {
            "message": "Firewall rule changed",
            "severity": "medium",
            "user": "root",
        },
    ]

    important_alerts = []
    privileged_users = ["admin", "root"]

    for alert in alerts:
        severity = alert["severity"]
        user = alert["user"]

        print(f'Reviewing: {alert["message"]}')

        if severity == "high" or severity == "critical":
            important_alerts.append(alert)
            print("  Important alert added")

        if user in privileged_users:
            print("  Privileged account involved")

    print("\nImportant-alert summary:")

    for alert in important_alerts:
        print(
            f'- {alert["severity"].upper()}: '
            f'{alert["message"]} ({alert["user"]})'
        )

    print("\nTotal alerts:", len(alerts))
    print("Important alerts:", len(important_alerts))

    # This example combines:
    # - Lists
    # - Dictionaries
    # - for loops
    # - if statements
    # - or
    # - in
    # - append()
    # - len()


# %% INVALID EXAMPLE NUMBER

if EXAMPLE_NUMBER < 1 or EXAMPLE_NUMBER > 16:
    print("Choose an EXAMPLE_NUMBER from 1 through 16.")


# =============================================================================
# COMMON BEGINNER MISTAKES
# =============================================================================

# 1. FORGETTING THE COLON
#
# Incorrect:
#
# for port in ports
#     print(port)
#
# Correct:
#
# for port in ports:
#     print(port)


# 2. INCORRECT INDENTATION
#
# Incorrect:
#
# for port in ports:
# print(port)
#
# Correct:
#
# for port in ports:
#     print(port)


# 3. USING AN INDEX THAT DOES NOT EXIST
#
# ports = [22, 80, 443]
#
# This causes an IndexError:
# print(ports[3])
#
# Valid indexes are 0, 1, and 2.


# 4. CREATING AN INFINITE WHILE LOOP
#
# attempt = 0
#
# This never changes attempt:
#
# while attempt < 3:
#     print("Trying again")
#
# Correct:
#
# while attempt < 3:
#     print("Trying again")
#     attempt += 1


# 5. MODIFYING A LIST WHILE LOOPING THROUGH IT
#
# This can produce confusing results:
#
# ports = [22, 80, 443, 3389]
#
# for port in ports:
#     if port == 80:
#         ports.remove(port)
#
# A clearer approach is to build a new filtered list:
#
# filtered_ports = []
#
# for port in ports:
#     if port != 80:
#         filtered_ports.append(port)


# 6. USING AN UNCLEAR LOOP VARIABLE
#
# Less clear:
#
# for x in ports:
#     print(x)
#
# Clearer:
#
# for port in ports:
#     print(port)


# =============================================================================
# ACTUAL FILE-READING VERSION
# =============================================================================

# AREPL demonstrations are easiest when they do not depend on an external file.
# To demonstrate a real file loop, place auth.log beside this Python file and
# run the following code in the VS Code terminal:
#
# with open("auth.log", "r", encoding="utf-8") as file:
#     for line in file:
#         if "Failed password" in line:
#             print(line.strip())
