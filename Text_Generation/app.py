import argparse
import logging
from data_loader import DataLoader
from chatbot import Chatbot
from story_generator import StoryGenerator
from joke_generator import JokeGenerator

# Setup logging
logging.basicConfig(
    filename="text_generation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    parser = argparse.ArgumentParser(description="Text Generation Project")
    parser.add_argument("--chatbot", action="store_true", help="Run the chatbot")
    parser.add_argument("--story", type=str, help="Generate a story with a given theme")
    parser.add_argument("--joke", action="store_true", help="Generate a random joke")
    args = parser.parse_args()

    data = DataLoader().data

    if args.chatbot:
        bot = Chatbot(data["chatbot"])
        print("Chatbot is ready! Type 'exit' to quit.")
        while True:
            user_text = input("You: ")
            if user_text.lower() == "exit":
                print("Bot: Goodbye!")
                break
            print("Bot:", bot.get_response(user_text))

    elif args.story:
        generator = StoryGenerator(data["stories"])
        print(generator.generate(args.story))

    elif args.joke:
        generator = JokeGenerator(data["jokes"])
        print(generator.generate())

    else:
        print("No option selected. Use --chatbot, --story <theme>, or --joke")

if __name__ == "__main__":
    main()





