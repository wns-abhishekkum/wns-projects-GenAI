import random


def chatbot_response(user_input: str) -> str:
    user_input = user_input.lower()

    #  rules
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm doing great, thanks!", "All good here. You?", "Better now that you asked!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Default fallback
    fallback = [
        "Interesting, tell me more!",
        "Hmm... I’ll have to think about that.",
        "Can you explain a bit more?",
        "That’s cool!"
    ]
    return random.choice(fallback)



def generate_story(theme: str) -> str:
    characters = ["a brave knight", "a clever fox", "a lost astronaut", "a curious child"]
    settings = ["in a dark forest", "on a distant planet", "inside a mysterious cave", "in an old library"]
    conflicts = ["faced a great challenge", "discovered a hidden secret", "had to make a tough choice", "met a strange new friend"]
    endings = ["and lived happily ever after.", "and learned something new.", "but the adventure had only just begun.", "and the story became a legend."]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    ending = random.choice(endings)

    story = f"Once upon a time, {character} {setting}. They {conflict}, {ending}"
    return f"Theme: {theme}\n{story}"



def generate_joke() -> str:
    setups = [
        "Why don’t scientists trust atoms?",
        "Why was the math book sad?",
        "Why don’t programmers like nature?",
        "What do you call fake spaghetti?"
    ]
    punchlines = [
        "Because they make up everything!",
        "Because it had too many problems.",
        "It has too many bugs.",
        "An impasta!"
    ]
    idx = random.randint(0, len(setups) - 1)
    return setups[idx] + " " + punchlines[idx]


# -------------------------------
if __name__ == "__main__":
    print("Simple Text Generation Project ===")
    while True:
        print("\nChoose an option:")
        print("1. Chatbot")
        print("2. Story Generator")
        print("3. Joke Generator")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_text = input("You: ")
            print("Bot:", chatbot_response(user_text))

        elif choice == "2":
            theme = input("Enter a theme for your story: ")
            print("\nGenerated Story:\n", generate_story(theme))

        elif choice == "3":
            print("\nHere's a joke:\n", generate_joke())

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
