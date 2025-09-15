# 📝 Text Generation Project

This project demonstrates **basic text generation techniques in Python**.  
It includes three fun mini-projects:
1. **Chatbot** – A simple rule-based chatbot that responds to user input.
2. **Story Generator** – Creates short random stories based on user-provided themes.
3. **Joke Generator** – Produces puns and one-liners.

---

## 🚀 Features
- **Chatbot**
  - Greets users
  - Responds to simple queries
  - Provides fallback responses for unknown input

- **Story Generator**
  - Randomly combines characters, settings, conflicts, and endings
  - Accepts a user-defined **theme**

- **Joke Generator**
  - Randomly picks from a list of joke setups and punchlines

---

 ![Image Alt](https://github.com/wns-abhishekkum/wns-projects-GenAI/blob/35f5f52970b4366b75f485aca6db5873d8a76580/Text_Generation/Screenshot%20(44).png)

## 🛠 Requirements
- Python **3.8+** (works on Python 3.12+ as well)
- No external libraries required (only uses Python standard library)

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/text-generation-project.git
   cd text-generation-project
   ```

2. Run the Python script:
   ```bash
   python app.py --joke
   python app.py --chatbot
   python app.py --story Adventure
   
   ```

3. Choose an option from the menu:
   ```
   === Simple Text Generation Project ===

   Choose an option:
   1. Chatbot
   2. Story Generator
   3. Joke Generator
   4. Exit
   ```

---

## 💡 Example Usage

### Chatbot
```
You: hello
Bot: Hi there!
```

### Story Generator
```
Theme: Adventure
Once upon a time, a curious child in an old library discovered a hidden secret, and the story became a legend.
```

### Joke Generator
```
Why don’t scientists trust atoms? Because they make up everything!
```

---

## 📂 Project Structure
```
text-generation-project/
│── app.py                 # Entry point (argparse, runs chatbot/story/joke)
│── chatbot.py              # Chatbot class
│── story_generator.py      # StoryGenerator class
│── joke_generator.py       # JokeGenerator class
│── data_loader.py          # DataLoader class
│── data.json               # (Optional) custom responses/stories/jokes
│── README.md               # Documentation
│── text_generation.log     # Log file (auto-created)

```

---

## 🤝 Contribution
Feel free to fork the repo, add more jokes, improve the chatbot rules, or expand the story generator!

---

## 📜 License
This project is licensed under the **MIT License** – free to use and modify.
