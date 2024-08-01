# Turtle Crossing Game

This is a simple Turtle Crossing game built using the `turtle` module in Python. The objective of the game is to guide the turtle across the road while avoiding the moving cars. As the player progresses, the speed and number of cars increase, making the game more challenging.

## Table of Contents

- [Game Features](#game-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Game Features

- **Player Control**: Use the "Up" arrow key to move the turtle forward.
- **Scoreboard**: Displays the current level.
- **Car Manager**: Generates and manages the movement of cars.
- **Level Progression**: Each time the turtle crosses the road successfully, the level increases and cars move faster.

## Requirements

- Python 3.x
- Turtle module (usually included with Python standard library)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Samuel-Abusa/turtle-crossing-game.git
    cd turtle-crossing-game
    ```

2. **Ensure all required files are present**:
    - `main.py`
    - `player.py`
    - `scoreboard.py`
    - `car_manager.py`

## How to Play

1. **Run the game**:
    ```sh
    python main.py
    ```

2. **Controls**:
    - Use the "Up" arrow key to move the turtle forward.
    - The turtle starts at the bottom of the screen and must reach the top to advance to the next level.

3. **Gameplay**:
    - Avoid getting hit by the cars.
    - Each successful crossing increases the level and the speed of the cars.
    - The game ends if the turtle collides with a car.

## Project Structure

```
turtle-crossing-game/
│
├── main.py         # Main game logic
├── player.py       # Player class
├── scoreboard.py   # Scoreboard class
└── car_manager.py  # CarManager class
```

### `main.py`

This file contains the main game loop, initializes the game screen, listens for player input, and handles the game logic.

### `player.py`

This file defines the `Player` class, which manages the turtle's movement and checks if the player has successfully crossed the road.

### `scoreboard.py`

This file defines the `Scoreboard` class, which handles the display and update of the game level.

### `car_manager.py`

This file defines the `CarManager` class, which generates and moves the cars across the screen. It also increases the car speed as the game progresses.

## Credits

This game was created using the `turtle` module in Python. Special thanks to all contributors and resources that helped in the development of this game.