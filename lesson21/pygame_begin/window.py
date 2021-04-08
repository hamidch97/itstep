import pygame

pygame.init()

(widh, high) = (500, 300)
background_color = (0, 0, 255)
bleu = (255, 255, 0)

screen = pygame.display.set_mode((widh, high))
screen.fill(background_color)
rect_form = (10, 10, 100, 100)
pygame.draw.rect(screen, bleu, rect_form)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
