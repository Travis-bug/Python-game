#!/usr/bin/env python3
"""
Terminal Snake Game
==================
Python Snake game implementation for the terminal using Python's curses library.

Controls:
- Arrow keys or WASD to move
- 'q' to quit
- Game automatically starts when run

Features:
- Growing snake when eating food
- Score tracking
- Game over detection
- Smoothish gameplay......
"""

import curses
import random
import time


class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sh, self.sw = stdscr.getmaxyx()
        self.w = curses.newwin(self.sh, self.sw, 0, 0)
        self.w.keypad(1)
        self.w.timeout(100)
        
        # Initialize snake in the middle of screen
        self.snake_x = self.sw // 4
        self.snake_y = self.sh // 2
        
        # Snake body - list of [y, x] coordinates
        self.snake = [
            [self.snake_y, self.snake_x],
            [self.snake_y, self.snake_x - 1],
            [self.snake_y, self.snake_x - 2]
        ]
        
        # First food
        self.food = [self.sh // 2, self.sw // 2]
        self.w.addch(int(self.food[0]), int(self.food[1]), curses.ACS_PI)
        
        # Initial direction (moving right)
        self.key = curses.KEY_RIGHT
        self.score = 0
        
    def create_food(self):
        """Create new food at random location"""
        food = None
        while food is None:
            nf = [
                random.randint(1, self.sh - 2),
                random.randint(1, self.sw - 2)
            ]
            food = nf if nf not in self.snake else None
        
        self.food = food
        self.w.addch(self.food[0], self.food[1], curses.ACS_PI)
    
    def update_score(self):
        """Update score display"""
        score_text = f"Score: {self.score}"
        self.w.addstr(0, 2, score_text)
    
    def game_over(self):
        """Display game over console and wait for user inout to restart or wuit"""
        self.w.clear()
        h, w = self.stdscr.getmaxyx()
        
        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {self.score}"
        restart_text = "Press 'r' to restart or 'q' to quit"
        
        # Center the text
        self.w.addstr(h//2 - 2, w//2 - len(game_over_text)//2, game_over_text)
        self.w.addstr(h//2, w//2 - len(final_score_text)//2, final_score_text)
        self.w.addstr(h//2 + 2, w//2 - len(restart_text)//2, restart_text)
        
        self.w.refresh()
        
        # Wait for user input
        while True:
            key = self.w.getch()
            if key == ord('q'):
                return False
            elif key == ord('r'):
                return True
    
    def run(self):
        """Main game loop"""
        while True:
            # Draw border
            self.w.border()
            
            # Update score
            self.update_score()
            
            # Get next key
            next_key = self.w.getch()
            
            # Set key if valid input received
            if next_key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT,
                           ord('s'), ord('w'), ord('a'), ord('d')]:
                self.key = next_key
            
            # Quit game
            if self.key == ord('q'):
                break
            
            # Calculate new head position based on curredt dir
            new_head = [self.snake[0][0], self.snake[0][1]]
            
            if self.key == curses.KEY_DOWN or self.key == ord('s'):
                new_head[0] += 1
            if self.key == curses.KEY_UP or self.key == ord('w'):
                new_head[0] -= 1
            if self.key == curses.KEY_LEFT or self.key == ord('a'):
                new_head[1] -= 1
            if self.key == curses.KEY_RIGHT or self.key == ord('d'):
                new_head[1] += 1
            
            # Insert new head
            self.snake.insert(0, new_head)
            
            # Check if snake hit the wall or itself
            if (new_head[0] in [0, self.sh - 1] or 
                new_head[1] in [0, self.sw - 1] or 
                new_head in self.snake[1:]):
                
                if self.game_over():
                    # Restart game
                    self.__init__(self.stdscr)
                    continue
                else:
                    break
            
            # Check if snake ate food and update score by one point  
            if self.snake[0] == self.food:
                self.score += 1
                self.create_food()
            else:
                # Remove tail if no food eaten
                tail = self.snake.pop()
                self.w.addch(int(tail[0]), int(tail[1]), ' ')
            
            # Draw snake on console screen
            self.w.addch(int(self.snake[0][0]), int(self.snake[0][1]), curses.ACS_CKBOARD)
            
            self.w.refresh()

def main(stdscr):
    """Main function to initialize curses and start game plau"""
    # Configure curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate
    
    # Start game
    game = SnakeGame(stdscr)
    
    # Show instructions
    h, w = stdscr.getmaxyx()
    Player_Manual = [
        "PYTHON SNAKE GAME",
        "",
        "Controls:",
        "Use the arrow keys or WASD to move",
        " Press'q' to quit",
        "",
        "Eat the food (π) to grow and score points!",
        "Don't hit the walls or yourself!",
        "",
        "Press any key to start..."
    ]

   # user_input = stdscr.getch() 
   # if user_input:   {i plan to add a feature where the user can press 'h' for help during the game, 
   # this featire pauses the game and resumes it after the 
   # use is done with reading, but for now this is just a placeholder }

   #i also plan to add a loading screen where the user reads the instructions 
   # while the game is loading, with some cool animations, 
   # feel free to suggest some ideas for the loading screen,
   # but for now this is just a placeholder P.S you can make these features if you want,
   #  just fork the repo and make your changes and open a pull request, i will review your changes before merging. THANKS :D
   
    
    stdscr.clear()
    for i, line in enumerate(Player_Manual):
        y = h//2 - len(Player_Manual)//2 + i
        x = w//2 - len(line)//2
        if 0 <= y < h and 0 <= x < w:
            stdscr.addstr(y, x, line[:w - x])
    stdscr.refresh()
    stdscr.getch()
    
    # Run the game
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
