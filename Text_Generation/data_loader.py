import json
import logging
from pathlib import Path

class DataLoader:
    def __init__(self, data_path="data.json"):
        self.data_path = Path(data_path)
        self.data = self._load_data()

    def _load_data(self):
        if not self.data_path.exists():
            logging.warning("Data file not found, using defaults")
            return {
                "chatbot": {
                    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
                    "how are you": ["I'm doing great, thanks!", "All good here. You?"],
                    "bye": ["Goodbye!", "See you later!", "Take care!"]
                },
                "stories": {
                    "characters": ["a brave knight", "a clever fox", "a lost astronaut", "a curious child"],
                    "settings": ["in a dark forest", "on a distant planet", "inside a mysterious cave", "in an old library"],
                    "conflicts": ["faced a great challenge", "discovered a hidden secret", "had to make a tough choice", "met a strange new friend"],
                    "endings": ["and lived happily ever after.", "and learned something new.", "but the adventure had only just begun.", "and the story became a legend."]
                },
                "jokes": {
                    "setups": [
                        "Why don’t scientists trust atoms?",
                        "Why was the math book sad?",
                        "Why don’t programmers like nature?",
                        "What do you call fake spaghetti?"
                    ],
                    "punchlines": [
                        "Because they make up everything!",
                        "Because it had too many problems.",
                        "It has too many bugs.",
                        "An impasta!"
                    ]
                }
            }
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to load data file: {e}")
            return {}




