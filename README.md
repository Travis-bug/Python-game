---
# Python Terminal Snake Game

A classic **Snake game** built in Python that runs directly in the terminal using the `curses` library.

The game recreates the traditional Snake gameplay with keyboard controls, score tracking, and collision detection.

---

## Features

* **Terminal-based gameplay**: No heavy graphics, just pure terminal logic.
* **Arrow keys or WASD movement**: Flexible control schemes for players.
* **Dynamic growth**: Snake grows longer every time food is eaten.
* **Score tracking**: Keep track of your progress in real-time.
* **Collision detection**: Logic for hitting walls or the snake's own body.
* **Game over screen**: Includes an option to restart immediately.
* **Smooth loop**: Optimized for a simple and smooth gameplay experience.

---

## Controls

| Key | Action |
| --- | --- |
| **Arrow Keys / WASD** | Move the snake |
| **Q** | Quit the game |
| **R** | Restart after game over |
| **H/P** | pause game for help screen | 

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Travis-bug/Python-game.git

```

### 2. Navigate to the project folder

```bash
cd Python-game

```

### 3. Run the game

```bash
python3 snake_game.py

```

---

## Requirements

* **Python 3.x**
* **Terminal that supports the `curses` library**

> [!NOTE]
> `curses` works natively on Linux and macOS.
> **Windows users** will need to install `windows-curses` via pip:
> ```bash
> pip install windows-curses
> 
> ```
> 
> 

---

## How the Game Works

* The snake moves continuously across the screen.
* Food appears randomly on the board.
* Eating food increases the snake's length and your score.
* Hitting a wall or the snake's own body ends the game.

---
## Game Play 

https://github.com/user-attachments/assets/60c4c88f-eb97-428e-9a9f-ae2053098374

___

## Project Structure

```text
Python-game
└──  snake_game.py
└──  README.md

```

---

## Planned Features

Future improvements for the project include:

* Pause / help menu during gameplay
* Loading screen with animation
* Difficulty levels
* High score tracking
* Improved UI elements

---

## Contributions

Contributions are welcome! Feel free to fork the repository, implement improvements, and open a pull request for review.

## License

This project is licensed under the **MIT License**.

---
