def classify_request(user_input):
    if "study" in user_input.lower():
        return "Study Assistant"
    elif "code" in user_input.lower():
        return "Coding Assistant"
    return "General Assistant"

user_input = input("Enter your request: ")
result = classify_request(user_input)

print(f"Selected workflow: {result}")
