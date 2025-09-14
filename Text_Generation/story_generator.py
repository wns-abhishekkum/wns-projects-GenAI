import random
import logging

class StoryGenerator:
    def __init__(self, story_data):
        self.characters = story_data["characters"]
        self.settings = story_data["settings"]
        self.conflicts = story_data["conflicts"]
        self.endings = story_data["endings"]

    def generate(self, theme: str) -> str:
        story = f"""
        Theme: {theme}
        Once upon a time, {random.choice(self.characters)} {random.choice(self.settings)}.
        They {random.choice(self.conflicts)}, {random.choice(self.endings)}
        """
        logging.info(f"Generated story for theme '{theme}'")
        return story.strip()
