import sys
import pygame
from settings import Setting
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Screen
        self.settings = Setting()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")
        # Ship
        self.ship = Ship(self)
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_event()
            # Update ship position every time
            self.ship.update()
            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_event(self):
        """Response to key press and mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move ship to right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move ship to left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    
    def _update_screen(self):
        """Update images to the screen, and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


