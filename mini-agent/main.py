def classify_request(user_input):
    text = user_input.lower()

    if "study" in text:
        return "Study Workflow"

    elif "code" in text:
        return "Coding Workflow"

    elif "productivity" in text:
        return "Productivity Workflow"

    return "General Workflow"

def validate_input(user_input):
    return len(user_input.strip()) > 0

def main():
    print("Mini AI Workflow Agent")

    user_input = input("Enter your request: ")

    if not validate_input(user_input):
        print("Invalid input.")
        return

    workflow = classify_request(user_input)

    print(f"Selected workflow: {workflow}")
    print("Response generated successfully.")

if __name__ == "__main__":
    main()
