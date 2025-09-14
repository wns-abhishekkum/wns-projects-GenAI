import random
import logging

class JokeGenerator:
    def __init__(self, jokes_data):
        self.setups = jokes_data["setups"]
        self.punchlines = jokes_data["punchlines"]

    def generate(self) -> str:
        idx = random.randint(0, len(self.setups) - 1)
        joke = self.setups[idx] + " " + self.punchlines[idx]
        logging.info(f"Generated joke: {joke}")
        return joke
