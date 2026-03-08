<details>
<summary><b>Click to view Development History & Bug Fixes</b></summary>

# View Errors, Fixes, and Commit Mapping

| Error / Change & Classification | Commit Type | The “Why” (Reasoning) | The Fix |
|---|---|---|---|
| 180-Degree Suicide (Logic Error) | refactor: | The code followed movement input but lacked rule enforcement to prevent reversing directly into the snake’s body. | Added directional guards (if/elif) to ignore inputs opposite to the current movement direction. |
| addstr() Out-of-Bounds (Bug) | fix: | A runtime _curses.error occurred when attempting to draw outside the terminal boundaries, causing crashes on smaller screens. | Implemented coordinate bounds checks and truncated strings before rendering (line[:w - x]). |
| Help Screen Flash (Input Handling Error) | refactor: | The help screen rendered but immediately returned to the game loop, making the instructions unreadable. | Switched to blocking input (timeout(-1)) and added a getch() call to pause until user input. |
| Invisible Snake Post-Help (State Error) | refactor: | Clearing the screen removed the visual snake while the internal snake position list remained unchanged. | Added a redraw loop to iterate through the snake segments and render them again after screen clears. |
| Duplicate Instruction Text (Code Duplication) | refactor: | Instruction/manual text existed in multiple places, increasing maintenance risk and violating DRY principles. | Moved instruction text into a shared global variable and reused it across help/loading screens. |
| Missing High Score System (Feature Gap) | feat: | The game tracked only the current score and lacked persistent performance tracking typical of arcade games. | Implemented high score tracking logic that updates when the current score exceeds the stored high score. |
| High Score Visibility (UX Improvement) | feat: | Players could not see their best score after a game ended, reducing replay incentive. | Added high score display to the game over screen. |
| Food Icon Clarity (Visual/UI Improvement) | style: | The previous symbol (ACS_PI) made the food difficult to visually distinguish from other elements. | Replaced the food symbol with ACS_DIAMOND for clearer visual representation. |


 </details>