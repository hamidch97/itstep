import pygame
import time

pygame.init()
(widh, high) = (500, 300)
bleu = (0, 0, 255)
yellow = (255, 255, 0)

screen = pygame.display.set_mode((widh, high))
screen.fill(bleu)


rect_form = pygame.Rect(10, 10, 50, 50)

pygame.draw.rect(screen, yellow, rect_form)

pygame.display.flip()
i = 0
while i < 100:
    time.sleep(.050)
    screen.fill(bleu)
    rect_form.width += 10
    rect_form.height += 10
    pygame.draw.rect(screen, yellow, rect_form)
    pygame.display.flip()
    i += 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
