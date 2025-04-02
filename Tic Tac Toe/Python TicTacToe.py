import pygame

pygame.init()

WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)
winner_text = font.render('', True, 'green')
textRect = winner_text.get_rect()
textRect.center = (WINDOW_WIDTH // 2 - PIXEL_WIDTH // 2, WINDOW_WIDTH // 2)

running = True

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)


ICON_X = load_icon('icons/x-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
ICON_O = load_icon('icons/o-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
GRID = load_icon('icons/grid.png', [WINDOW_WIDTH, WINDOW_WIDTH])

PLAYER_1 = 0
PLAYER_2 = 1
player = PLAYER_1


def play_turn(current_player):
    curr_coordinate = pygame.math.Vector2(pygame.mouse.get_pos())
    normalized_coordinate = curr_coordinate // PIXEL_WIDTH
    if pygame.mouse.get_pressed()[0]:
        col, row = map(int, normalized_coordinate)
        board[row][col] = current_player
        global player
        player = 1 - player


def draw_icons():
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            if board[i][j] == 0:
                screen.blit(ICON_O, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))
            if board[i][j] == 1:
                screen.blit(ICON_X, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))


def has_equal_icons(elements, game_player):
    for element in elements:
        if element != game_player:
            return False
    return True


def has_winning_row(game_player):
    return has_equal_icons(board[0], game_player) \
        or has_equal_icons(board[1], game_player) \
        or has_equal_icons(board[2], game_player)


def has_winning_col(game_player):
    return has_equal_icons([board[0][0], board[1][0], board[2][0]], game_player) \
        or has_equal_icons([board[0][1], board[1][1], board[2][1]], game_player) \
        or has_equal_icons([board[0][2], board[1][2], board[2][2]], game_player)


def has_winning_diagonal(game_player):
    return has_equal_icons([board[0][0], board[1][1], board[2][2]], game_player) \
        or has_equal_icons([board[0][2], board[1][1], board[2][0]], game_player)


def is_winner(game_player):
    return has_winning_row(game_player) \
        or has_winning_col(game_player) \
        or has_winning_diagonal(game_player)


def check_victory():
    global winner_text
    if is_winner(PLAYER_1):
        winner_text = font.render('Player 1 WON!', True, 'green')
        return True
    if is_winner(PLAYER_2):
        winner_text = font.render('Player 2 WON!', True, 'green')
        return True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    pygame.display.flip()
    screen.fill("white")
    screen.blit(GRID, (0, 0))
    pygame.event.wait()
    play_turn(player)
    draw_icons()
    if check_victory():
        screen.blit(winner_text, textRect)

pygame.quit()