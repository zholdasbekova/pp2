import pygame
import sys
import random
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Load images
player_img = pygame.image.load("pic/Player.png")
enemy_img = pygame.image.load("pic/Enemy.png")
coin_img = pygame.image.load("pic/Coin.png")

scaled_player = pygame.transform.scale(player_img, (45, 60))
scaled_enemy = pygame.transform.scale(enemy_img, (45, 60))
scaled_coin = pygame.transform.scale(coin_img, (35, 35))

# Font settings for displaying coins collected
font = pygame.font.Font(None, 36)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scaled_enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scaled_player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scaled_coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.center = (random.randint(30, 370), -50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Initialize player, enemy, and coin objects
player = Player()
enemy = Enemy()
coin = Coin()

# Counter for collected coins
coins_collected = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    enemy.move()
    coin.move()

    # Collision detection between player and coin
    if pygame.sprite.collide_rect(player, coin):
        coins_collected += 1
        # After collision, reposition the coin
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    # Collision detection between player and enemy
    if pygame.sprite.collide_rect(player, enemy):
        print("Game Over")  # You can replace this with game over screen or logic
        pygame.quit()
        sys.exit()

    DISPLAYSURF.fill(WHITE)
    player.draw(DISPLAYSURF)
    enemy.draw(DISPLAYSURF)
    coin.draw(DISPLAYSURF)

    # Display collected coins count in the top right corner
    coin_text = font.render("Coins: " + str(coins_collected), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
