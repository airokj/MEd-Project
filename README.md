# MEd Thesis Physics Game

Educational physics video game developed as part of a Master's thesis.

## Purpose
- Improve student motivation
- Connect physics variables to observable phenomena
- Support pre/post-test research design

## Built With
- Python
- Pygame (within Python)

## Structure
audio/     → sound effects & music
graphics/  → sprites and UI
code/      → game logic
map/       → level data

## Important Game Logic
Most of the game logic cycles between 3 files in the code folder
main.py runs the whole thing
enemy.py runs the enemy logic, and how they respond to player attacks
player.py runs the user, and any user controls
level.py ties the enemy and the player together on a single map that is generated all at once.
The other files are also critical to the program, but are mostly for game logic, and less for the specific rules of this thesis project. 
