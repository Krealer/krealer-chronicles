# 🎮 Krealer Chronicles

**Krealer Chronicles** is a Python-based 2D game created with `pygame`, featuring maze navigation and turn-based combat. Built as part of a broader journey to explore game development across multiple languages, this project is the first chapter starring the character **Krealer**.

---

## 🧩 Features

- Sprite-based movement and animation
- Maze generation using grid-based layout
- Collision detection with walls and goals
- Turn-based combat system with:
  - Skills, healing, and effects
  - Conditional abilities (reflection, debuffs, power scaling)
- Modular code (player, enemy, settings, battle logic)
- Simple key-controlled UI (no mouse needed)

---

## 🕹️ Controls

| Key | Action                  |
|-----|--------------------------|
| Arrow Keys / WASD | Move Krealer          |
| 1   | Use first battle skill (!?!?)      |
| 2   | Absorb (damage + heal) |
| 3   | Gain a UP point         |
| 4   | Storm of Code (use all UP points) |
| SPACE | Advance to next turn/message |
| ESC | Quit the game           |

---

## 🛠️ Setup Instructions

### Requirements
- Python 3.12+
- `pygame`

### Installation

```bash
# Clone the repo
git clone git@github.com:yourusername/krealer-chronicles.git
cd krealer-chronicles

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
