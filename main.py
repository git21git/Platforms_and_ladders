import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Лесенки')
all_sprites = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ladders_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, mouse_pos):
        super().__init__(all_sprites)
        self.add(player_group, all_sprites)
        x, y = mouse_pos
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color("Blue"))
        self.rect = pygame.Rect(x, y, 20, 20)

    def update(self, direction='down'):
        if not (pygame.sprite.spritecollideany(self, platform_group) or
                pygame.sprite.spritecollideany(self, ladders_group)):
            self.rect = self.rect.move(0, 2)
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, ladders_group):
            if keys[pygame.K_UP]:
                self.rect = self.rect.move(0, -10)
            if keys[pygame.K_DOWN]:
                self.rect = self.rect.move(0, 10)
        if keys[pygame.K_LEFT]:
            self.rect = self.rect.move(-10, 0)
        if keys[pygame.K_RIGHT]:
            self.rect = self.rect.move(10, 0)


class Platform(pygame.sprite.Sprite):
    image = pygame.Surface([50, 10])

    def __init__(self, mouse_pos):
        super().__init__(all_sprites)
        x, y = mouse_pos
        self.add(platform_group, all_sprites)
        self.image.fill(pygame.Color("Grey"))
        self.rect = pygame.Rect(x, y, 50, 10)


class Ladders(pygame.sprite.Sprite):
    image = pygame.Surface([10, 50])

    def __init__(self, mouse_pos):
        super().__init__(all_sprites)
        x, y = mouse_pos
        self.add(ladders_group, all_sprites)
        self.image.fill(pygame.Color("Red"))
        self.rect = pygame.Rect(x, y, 10, 50)


def main():
    fps = 30
    clock = pygame.time.Clock()
    running = True
    player = None
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                keys = pygame.key.get_pressed()
                if event.button == 1 and keys[pygame.K_LCTRL]:
                    Ladders(pygame.mouse.get_pos())
                elif event.button == 3:  # Правая
                    if not player:
                        player = Player(pygame.mouse.get_pos())
                    else:
                        x, y = pygame.mouse.get_pos()
                        player.rect = pygame.Rect(x, y, 20, 20)
                elif event.button == 1:  # Левая
                    Platform(pygame.mouse.get_pos())

        screen.fill(pygame.Color("black"))
        player_group.update()
        player_group.draw(screen)
        platform_group.draw(screen)
        ladders_group.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
