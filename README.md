# Asteroid Game

This is a simple asteroid game implemented using Python and Pygame. The player controls a spaceship that can move and shoot to destroy asteroids. The game ends when the player's spaceship collides with an asteroid.

## Requirements

- Python 3.12
- Pygame 2.6.1

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Maik-Schulze/asteroids
    cd asteroids
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the game using the following command:
```sh
python main.py
```

## Controls

- `W`: Move forwards
- `S`: Move backwards
- `A`: Rotate left
- `D`: Rotate right
- `SPACE`: Shoot

## Project Structure

- main.py
: The main entry point of the game.

- player.py
: Contains the Player class which defines the player's spaceship.

- asteroid.py
: Contains the Asteroid class which defines the asteroids.

- asteroidfield.py
: Contains the AsteroidField class which manages the spawning of asteroids.

- circleshape.py
: Contains the CircleShape base class for circular game objects.

- constants.py
: Contains game constants such as screen dimensions and asteroid spawn rate.

- shot.py
: Contains the Shot class which defines the shots fired by the player.

- requirements.txt
: Lists the required Python packages.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
