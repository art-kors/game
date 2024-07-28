import random
import pygame
import sys
import os
import main
import pygame_gui
WIDTH = 480
HEIGHT = 600
FPS = 60


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def game_over(winner, screen):
    manager = pygame_gui.UIManager((480, 600))
    resume = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((125, 175), (110, 25)),
        text='продолжить',
        manager=manager
    )
    win = f'                                 {winner}'
    menu = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((125, 100), (110, 25)),
        text=f'меню',
        manager=manager
    )
    fon = pygame.transform.scale(load_image('fone.jpg'), (1000, 1000))
    clock = pygame.time.Clock()
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == resume:
                        return reversi() # начинаем игру
                    elif event.ui_element == menu:
                        menu_alpha_ver.main()
            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(fon, (0, 0))
        win = f'                                 {winner}'
        intro_text = ["", "",
                      "", '', '', '', win,
                      '']
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        manager.draw_ui(screen)
        pygame.display.flip()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        gen_sp = []
        self.board = []
        for i in range(self.height):
            for j in range(self.width):
                gen = random.randint(0, 1)
                gen_sp.append(gen)
            self.board.append(gen_sp)
            gen_sp = []
        print(self.board)
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.turn = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color(0, 0, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell):
        print('click:', cell)
        if self.turn == 0:
            for i in range(self.width):
                self.board[cell[1]][i] = 0
            for j in range(self.height):
                self.board[j][cell[0]] = 0
            self.turn = 1
        elif self.turn == 1:
            for i in range(self.width):
                self.board[cell[1]][i] = 1
            for j in range(self.height):
                self.board[j][cell[0]] = 1
            self.turn = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
        else:
            pass

    def is_winner(self):
        red = 0
        winner = ''
        blue = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 1:
                    red += 1
                else:
                    blue += 1
        if red > blue and blue == 0:
            winner = 'blue win'
        elif blue > red and red == 0:
            winner = 'red win'
        return winner


def reversi():
    pygame.init()
    width, height = 480, 600
    size = width, height
    screen = pygame.display.set_mode(size)
    background = pygame.Surface((480, 600))
    background.fill(pygame.Color('white'))
    board = Board(8, 8)

    manager = pygame_gui.UIManager((480, 600))
    exit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 325), (110, 25)),
        text='exit',
        manager=manager
    )

    menu = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((200, 325), (110, 25)),
        text='menu',
        manager=manager
    )

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                board.get_click((x, y))
            if board.is_winner():
                win = board.is_winner()
                game_over(win, screen)
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == menu:
                        menu_alpha_ver.main()
                    elif event.ui_element == exit:
                        pygame.quit()
                        sys.exit()
            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(background, (0, 0))
        board.render(screen)
        manager.draw_ui(screen)
        pygame.display.flip()


if __name__ == '__main__':
    reversi()