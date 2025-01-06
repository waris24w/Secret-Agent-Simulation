import string
import random

# Define characters for secret name
chars = string.digits

# Storing user info in a dictionary
user_info = {}

# Fake names and addresses
fake_towns = ["Berlin", "Bonn", "Trier", "Bochum", "Augsburg"]
fake_postals = ["10607", "1039", "78229", "5516", "10963", "1749"]

# Agent roles
agent_roles = {"1": "Detective", "2": "Informer"}

# Questions for each role
question1 = {
    "1": "What is the capital of France?",
    "2": "What is the largest mammal on Earth?",
    "3": "What is the largest ocean on Earth?",
    "4": "What is the tallest land animal on Earth?",
}

question2 = {
    "1": "What's the full name of Sherlock?",
    "2": "What is Sherlock's IQ?",
    "3": "Who is smarter, Enola or Sherlock?",
}

# Shuffle fake towns and postals
random.shuffle(fake_towns)
random.shuffle(fake_postals)


# Function to generate secret name and address
def name_gen():
    secret_name = "".join(random.choice(chars) for _ in range(3))
    print("\nHere is your Secret Name & Address:")
    print("-----------------------------------")
    print(f"Name: {secret_name}")
    print(f"Town: {fake_towns[0]}")
    print(f"Postal Code: {fake_postals[0]}")
    print("-----------------------------------")


# Function to display roles and responsibilities
def roles_respon():
    print("\n---------Roles & Responsibilities--------")
    for key, value in agent_roles.items():
        print(f"{key}: {value}")
    print("----------------------------------------")


# Function for detective questions
def question_detective():
    score = 0
    wrong = 0
    for i, (key, question) in enumerate(question1.items(), start=1):
        print(question)
        answer = input("Enter Answer: ").strip().lower()
        if (i == 1 and answer == "paris") or \
           (i == 2 and answer == "blue whale") or \
           (i == 3 and answer == "pacific ocean") or \
           (i == 4 and answer == "giraffe"):
            print("\tCorrect")
            score += 1
        else:
            print("\tWrong :(")
            wrong += 1

    display_result(score, wrong, "Detective")


# Function for informer questions
def informer_question():
    score = 0
    wrong = 0
    for i, (key, question) in enumerate(question2.items(), start=1):
        print(question)
        answer = input("Enter Answer: ").strip().lower()
        if (i == 1 and answer == "william sherlock scott") or \
           (i == 2 and answer == "190") or \
           (i == 3 and answer == "enola"):
            print("\tCorrect")
            score += 1
        else:
            print("\tWrong :(")
            wrong += 1

    display_result(score, wrong, "Informer")


# Function to display result
def display_result(score, wrong, role):
    print("\n---------- Result ---------------")
    if score >= 2:
        print(f"Congratulations! You have successfully passed the {role} test.")
    else:
        print(f"Sorry, you failed the {role} test.")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {wrong}")
    print("---------------------------------")


# Main program loop
running = True
while running:
    print("\nDo you want to join the Secret Service? (y/n)")
    confirm = input().strip().lower()
    if confirm == "n":
        print("OK, no problem. Have a good day!")
        break
    elif confirm == "y":
        print("\nAlright! But we need your original name and address.")
        name = input("Enter your name: ").strip()
        address = input("Enter your address: ").strip()
        user_info["name"] = name
        user_info["address"] = address

        name_gen()  # Generate secret name and address
        roles_respon()  # Display roles and responsibilities

        role_choice = input("Select your role (1 for Detective, 2 for Informer): ").strip()
        if role_choice == "1":
            print(f"\nYou chose to become a {agent_roles[role_choice]}.")
            print("To become a Detective, you need to pass a 4-question test.\n")
            question_detective()
        elif role_choice == "2":
            print(f"\nYou chose to become a {agent_roles[role_choice]}.")
            print("To become an Informer, you need to pass a 3-question test.\n")
            informer_question()
        else:
            print("Invalid role selection. Please restart the program.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
