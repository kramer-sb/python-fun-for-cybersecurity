import string
# The string module includes helpful character groups and lets us format parts of our strings

def check_password_strength(password):
    score = 0
    feedback = []

# check length
    if len(password) >= 16:
        score += 1
    else:
        feedback.append("Use at least 16 characters.")
# check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
#Check Uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")
#Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")
#Check symbols
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one symbol.")
# Decide strength level
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else: 
        strength = "Weak"
    return strength, score, feedback   

# Ask for input

password = input("Enter a fake test password: ")

strength, score, feedback, = check_password_strength(password)

#Print statements

print(f"Password strength: {strength}")
print(f"Score: {score}/5)")

#Print Recommendations
if feedback:
    print("Recommendations:")

    for item in feedback:
        print(f"- {item}")
else:
    print("Nice work. This test password passed all checks. ")