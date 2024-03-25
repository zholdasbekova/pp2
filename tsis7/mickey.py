import pygame
import sys
import math
import os

def load_image(image_path):
    try:
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print("Cannot load image:", image_path)
        raise SystemExit(str(e))

def main():
    pygame.init()

    window_size = (600, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Mickey Clock')

    mickey_image = load_image(os.path.join("Pictures", "mickeyclock.jpeg"))
    mickey_rect = mickey_image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        current_time = pygame.time.get_ticks() // 1000 
        seconds_angle = current_time % 60 * 6  
        minutes_angle = current_time % 3600 // 60 * 6  

        mickey_seconds = pygame.transform.rotate(mickey_image, -seconds_angle)
        mickey_minutes = pygame.transform.rotate(mickey_image, -minutes_angle)

        screen.blit(mickey_seconds, mickey_rect)
        screen.blit(mickey_minutes, mickey_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    main()