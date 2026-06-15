import pygame
import sys

# Oyun parametrləri
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Blokun başlanğıc mövqeyi
    block_x = SCREEN_WIDTH // 2
    block_y = SCREEN_HEIGHT - BLOCK_SIZE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # İdarəetmə
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and block_x > 0:
            block_x -= 5
        if keys[pygame.K_RIGHT] and block_x < SCREEN_WIDTH - BLOCK_SIZE:
            block_x += 5

        # Ekranı yenilə
        screen.fill((0, 0, 0)) # Qara fon
        pygame.draw.rect(screen, BLUE, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
