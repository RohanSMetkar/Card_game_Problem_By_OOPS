# 🃏 War Card Game (Python OOP)

A simple **two-player War card game** implemented in **Python using Object-Oriented Programming (OOP)**.

This project simulates the classic card game **War**, where two players draw cards from their decks and the player with the higher card wins the round. If both cards have the same value, a **WAR** occurs and additional cards are drawn to determine the winner.

---

# 📌 Features

* Built using **Python classes**
* Uses **Object-Oriented Programming concepts**
* Simulates a full **52-card deck**
* Supports **two real players**
* Handles **WAR situations automatically**
* Runs in the **terminal / command line**

---

# 🧠 OOP Concepts Used

This project demonstrates several important OOP principles:

* **Classes and Objects**
* **Encapsulation**
* **Class Methods**
* **Instance Variables**
* **Interaction between multiple classes**

Classes used in the project:

* `Card` – represents a single playing card
* `Deck` – creates and shuffles a deck of cards
* `Player` – stores and manages each player's cards

---

# 🎮 How the Game Works

1. The deck is shuffled.
2. Each player receives **26 cards**.
3. In each round:

   * Both players draw the top card.
   * The player with the higher card wins the round.
4. If both cards are equal:

   * A **WAR** occurs.
   * Each player places additional cards.
5. The winner collects all cards from the round.
6. The game continues until one player runs out of cards.

---

# ▶️ How to Run the Game

### 1. Clone the repository

```bash
git clone https://github.com/your-username/war-card-game.git
```

### 2. Navigate to the project folder

```bash
cd war-card-game
```

### 3. Run the program

```bash
python war_game.py
```

---

# 🖥 Example Gameplay

```
WELCOME TO THE WAR CARD GAME

Enter Player 1 name: Alice
Enter Player 2 name: Bob

Round 1

Alice played: Ten of Hearts
Bob played: Eight of Clubs

Alice wins the round!
```

---

# 📁 Project Structure

```
war-card-game/
│
├── war_game.py      # Main game file
└── README.md        # Project documentation
```

---

# 🚀 Future Improvements

Possible upgrades for the project:

* Add **graphical interface (GUI)**
* Add **score tracking**
* Add **animations or card visuals**
* Implement **online multiplayer**
* Add **AI opponent**

---

# 👨‍💻 Author

Developed as a **Python OOP practice project** to demonstrate class-based design and game logic.

---

# 📜 License

This project is open-source and available for learning and educational purposes.

