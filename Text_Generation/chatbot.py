import random
import logging

class Chatbot:
    def __init__(self, responses):
        self.responses = responses
        self.context = []

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()
        self.context.append(user_input)

        for key, answers in self.responses.items():
            if key in user_input:
                reply = random.choice(answers)
                logging.info(f"Chatbot reply: {reply}")
                return reply

        # Context-based: If user repeats same question
        if len(self.context) > 1 and self.context[-1] == self.context[-2]:
            return "You already asked that, let’s talk about something else!"

        fallback = [
            "Interesting, tell me more!",
            "Hmm... I’ll have to think about that.",
            "Can you explain a bit more?",
            "That’s cool!"
        ]
        return random.choice(fallback)
