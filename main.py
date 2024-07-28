import sys
import pygame
import reversi
import pygame_gui
import shmup


def main():
    pygame.init()
    pygame.display.set_caption('MULTIVERSE')

    window_surface = pygame.display.set_mode((480, 600))
    manager = pygame_gui.UIManager((480, 600))
    color = 'white'
    exit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((200, 400), (100, 50)),
        text='exit',
        manager=manager
    )

    rev = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((110, 200), (100, 50)),
        text='reversi',
        manager=manager
    )
    shmp = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((260, 200), (100, 50)),
        text='shmup!',
        manager=manager
    )

    background = pygame.Surface((480, 600))
    background.fill(pygame.Color('white'))
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == exit:
                        pygame.quit()
                        sys.exit()
                    if event.ui_element == rev:
                        reversi.reversi()
                    if event.ui_element == shmp:
                        shmup.game()
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()


if __name__ == '__main__':
    main()