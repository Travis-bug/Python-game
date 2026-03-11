<details>
<summary><b>Click to view Development History & Bug Fixes</b></summary>

# Developement History Bug Fixes, and Commit Mapping

| Error / Change & Classification | Commit Type | The “Why” (Reasoning) | The Fix |
|---|---|---|---|
| 180-Degree Suicide (Logic Error) | refactor: | The code followed movement input but lacked rule enforcement to prevent reversing directly into the snake’s body. | Added directional guards (if/elif) to ignore inputs opposite to the current movement direction. |
| addstr() Out-of-Bounds (Bug) | fix: | A runtime `_curses.error` occurred when attempting to draw outside the terminal boundaries, causing crashes on smaller screens. | Implemented coordinate bounds checks and truncated strings before rendering (`line[:w - x]`). |
| Help Screen Flash (Input Handling Error) | refactor: | The help screen rendered but immediately returned to the game loop, making the instructions unreadable. | Switched to blocking input (`timeout(-1)`) and added a `getch()` call to pause until user input. |
| Invisible Snake Post-Help (State Error) | refactor: | Clearing the screen removed the visual snake while the internal snake position list remained unchanged. | Added a redraw loop to iterate through the snake segments and render them again after screen clears. |
| Duplicate Instruction Text (Code Duplication) | refactor: | Instruction/manual text existed in multiple places, increasing maintenance risk and violating DRY principles. | Moved instruction text into a shared global variable and reused it across help/loading screens. |
| Missing High Score System (Feature Gap) | feat: | The game tracked only the current score and lacked persistent performance tracking typical of arcade games. | Implemented high score tracking logic that updates when the current score exceeds the stored high score and stores it in a binary file using `pickle`. |
| High Score Visibility (UX Improvement) | feat: | Players could not see their best score after a game ended, reducing replay incentive. | Added high score display to the game over screen. |
| Food Icon Clarity (Visual/UI Improvement) | style: | The previous symbol (`ACS_PI`) made the food difficult to visually distinguish from other elements. | Replaced the food symbol with `ACS_DIAMOND` for clearer visual representation. |
| Sound System Introduction (New Feature) | feat: | The game previously had no audio feedback, reducing immersion and feedback during state changes. | Implemented a `BackgroundSound` class using `pygame.mixer` with state-based music switching (loading, gameplay, pause, game over). |
| Loading Screen Music Not Playing (Logic Bug) | fix: | The sound manager initialized with `present_state = "Loading_screen"`. When `change_state("Loading_screen")` was called, the function exited early because the new state matched the current state. | Set `present_state = None` during initialization so the first state change always loads and plays music. |
| Pause Music Persisting After Help Screen (State Transition Bug) | fix: | The help screen triggered pause music but never restored the gameplay track after exiting the help screen. | Added `bg.change_state("Game_Play")` immediately after leaving the help screen. |
| Sound Files Not Found (Path Resolution Issue) | fix: | Audio files stored in a nested `assets/sounds` directory were not always detected depending on the working directory. | Updated file paths to explicit relative paths (`assets/sounds/filename.wav`). |
| Audio Crash Risk When File Missing (Stability Issue) | refactor: | `pygame.mixer.music.load()` throws an exception if a file path is invalid, which could terminate the program. | Added optional file existence checks using `os.path.exists()` before attempting to load audio. | 
|

 </details>