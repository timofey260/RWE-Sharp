import pygame
import sys


pygame.init()


IMAGE_PATH = r"C:\part7.png"  # Replace with your image path

# Define the window size
WINDOW_WIDTH = 190
WINDOW_HEIGHT = 220

image = pygame.image.load(IMAGE_PATH)
image_rect = image.get_rect()

screen = pygame.display.set_mode((image_rect.width, image_rect.height))
pygame.display.set_caption("Image Snipper")

window_x, window_y = 0, 0

def save_snip(image, x, y, width, height, count):
    sub_surface = image.subsurface((x, y, width, height))
    pygame.image.save(sub_surface, f"snip_{count}.png")


running = True
snip_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Press 'S' to save the snip
                save_snip(image, window_x, window_y, WINDOW_WIDTH, WINDOW_HEIGHT, snip_count)
                snip_count += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                window_x, window_y = pygame.mouse.get_pos()


    window_x = max(0, min(window_x, image_rect.width - WINDOW_WIDTH))
    window_y = max(0, min(window_y, image_rect.height - WINDOW_HEIGHT))

    # Draw everything
    screen.blit(image, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (window_x, window_y, WINDOW_WIDTH, WINDOW_HEIGHT), 2)


    pygame.display.flip()


pygame.quit()
sys.exit()