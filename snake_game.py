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


High_score = 0 
help_text = [
            "HELP - SNAKE GAME",
            "-------------------",
            "CONTROLS:",
            "", 
            "Arrow keys/ WASD : Move",
            "Press 'q or Q'   :  quit",
            "press 'h or H'   :  help",
            "---------------------------",
            "INSTRUCTIONS:",
            "",
            "Eat the food (π) to grow and score points!",
            "The more you eat, the longer you grow!",
            "Don't hit the walls or yourself!",
            "",
            "Press any key to return to the game..."
        ]


class SnakeGame:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sh, self.sw = stdscr.getmaxyx()
        self.w = curses.newwin(self.sh, self.sw, 0, 0)
        self.w.keypad(1)
        self.w.timeout(100)  # Refresh every 100ms
        
        
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
        self.w.addch(int(self.food[0]), int(self.food[1]), curses.ACS_DIAMOND)
        
        # Initial direction (moving right)
        self.key = curses.KEY_RIGHT
        self.score = 0
       
        



    def create_food(self):
        """Create new food at random location"""
        food = None
        while food is None:
            new_food = [
                random.randint(1, self.sh - 2),
                random.randint(1, self.sw - 2)
            ]
            food = new_food if new_food not in self.snake else None
        
        self.food = food
        self.w.addch(self.food[0], self.food[1], curses.ACS_DIAMOND)



    def help_screen(self): 
        """Display help screen and wait for user input to return to game"""
    
        h, w = self.stdscr.getmaxyx() #
        self.w.timeout(-1) # Wait indefinitely for user input
        
        for i, line in enumerate(help_text):
            y = h//2 - len(help_text)//2 + i
            x = w//2 - len(line)//2

            if 0 <= y < h and 0 <= x < w:
             
             self.w.addstr(y, x, line[:w - x])
        self.w.refresh()
        curses.flushinp()   # clear leftover input
        self.w.getch()      # wait for user to press a key

        self.w.timeout(100) # restore game speed
        self.w.clear()  # Clear help screen and return to game
        self.w.addch(self.food[0], self.food[1], curses.ACS_DIAMOND) # Redraw food after clearing screen
        for segment in self.snake:
            self.w.addch(int(segment[0]), int(segment[1]), curses.ACS_CKBOARD)
    




    def update_score(self):
        """Update score display"""
        score_text = f"Score: {self.score}"
        self.w.addstr(0, 2, score_text)



    def get_high_score(self):
        global High_score
        if self.score > High_score:
            High_score = self.score
        return High_score





    def game_over(self):
        """Display game over console and wait for user inout to restart or wuit"""
        self.w.clear()
        h, w = self.stdscr.getmaxyx()
        
        game_over_msg = "GAME OVER!"
        final_score_msg = f"Final Score: {self.score}"
        restart_msg = "Press 'r' to restart or 'q' to quit"
        high_score_msg = f"High score: {self.get_high_score()}"
        
    
        # Center the texts 
        self.w.addstr(h//2 - 2, w//2 - len(game_over_msg)//2, game_over_msg)
        self.w.addstr(h//2, w//2 - len(final_score_msg)//2, final_score_msg)
        self.w.addstr(h//2 + 2, w//2 - len(restart_msg)//2, restart_msg)
        self.w .addstr(h//2 + 4, w//2 - len(high_score_msg)// 2, high_score_msg)
        
        self.w.refresh()
        
        # Wait for user input
        while True:
            key = self.w.getch()
            if key == ord ('q') or key == ord ('Q'):
                return False
            elif key == ord ('r') or key == ord ('R'):
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
            

            if next_key in [ord('h'), ord('H'), ord('p'), ord('P')]:
                self.help_screen()

                continue



#---------------------------------GAME LOGIC------------------
            # Set key if valid input received
            if next_key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT,
                           ord('s'), ord('w'), ord('a'), ord('d')]:
                self.key = next_key
            
#----------------------------to prevent the snake from reversing direction 9to be refactored to stop 180 suicide error----------------------





            # Quit game
            if next_key == ord('q'):
                self.game_over()
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



def loading_screen(stdscr):
    """Display loading screen with animation"""
    h, w = stdscr.getmaxyx()
    loading_text = "LOADING PYTHON..."
    bar_width = 30

    for i in range(bar_width + 1):
        stdscr.clear()
        progress = (i / bar_width)
        bar = "█" * i + "-" * (bar_width - i)
        stdscr.addstr(h//2, w//2 - len(loading_text)//2, loading_text)
        stdscr.addstr(h//2 + 2, w//2 - 2 - (bar_width//2), f"[{bar}] {int(progress*100)}%")
        stdscr.refresh()
        time.sleep(0.1) # Simulate loading speed





def main(stdscr):
    curses.curs_set(0)
    
    
    # 1. Show Loading Screen
    loading_screen(stdscr)
   

    # Show instructions
    
   # {i plan to add a feature where the user can press 'h' for help during the game, 
   # this featire pauses the game and resumes it after the   
   # user is done with reading, but for now this is just a placeholde} =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> completed 

   # {i also plan to add a loading screen where the user reads the instructions 
   # while the game is loading, with some cool animations} =>>>>>>>>>>>>>>>>> completed 

   # feel free to suggest some ideas for the loading screen,
   # but for now this is just a placeholder P.S you can make these features if you want,
   # just fork the repo and make your changes and open a pull request, i will review your changes before merging. THANKS :D
   
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    for i, line in enumerate(help_text):
        y = h//2 - len(help_text)//2 + i
        x = w//2 - len(line)//2
        if 0 <= y < h and 0 <= x < w:
            stdscr.addstr(y, x, line[:w - x])
    stdscr.refresh()
    stdscr.getch()
    

    # Start game
    game = SnakeGame(stdscr)
    # Run the game
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
