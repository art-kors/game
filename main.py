import pygame
import os
import sys
import random
pygame.init()
FPS = 50
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
huy = 15

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 20

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.x = x
        self.rect.y = y


if __name__ == "__main__":
    clock = pygame.time.Clock()
    width, height = 600, 600
    size = width, height
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    Arrow(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif pygame.mouse.get_focused():
                all_sprites.draw(screen)
                all_sprites.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

