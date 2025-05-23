import pygame

class Ship:
    """A class to manage ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start the ship from bottom middle
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at the defined location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update ships position based on movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    