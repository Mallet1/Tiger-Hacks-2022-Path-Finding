import pygame, sys
from PIL import Image

def draw_grid():
    rows = len(matrix)

    gap = WIDTH // rows
    for i in range(rows+1):
        pygame.draw.line(screen, (128, 128, 128), (0, i * gap), (WIDTH, i * gap))
        for j in range(rows+1):
            pygame.draw.line(screen, (128, 128, 128), (j * gap, 0), (j * gap, WIDTH))

def display_clicked():
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            if matrix[i][k] == 1:
                pygame.draw.rect(screen, (128, 128, 128), ((CELL_SIZE * (k)), (CELL_SIZE * (i)), CELL_SIZE, CELL_SIZE))

def printMatrix():
    print('[')
    for i in range(len(matrix)):
        print('[', end='')
        for k in range(len(matrix[0])):
            print(f'{matrix[i][k]}, ', end='')
        print('],')

    print(']\n\n\n')

img = Image.open("map.jpg")

WIDTH, HEIGHT = img.size # MU Map is 1000 X 1000
CELL_SIZE = WIDTH // 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg_surf = pygame.image.load('map.jpg').convert()
matrix = [[0 for i in range(WIDTH // CELL_SIZE)] for k in range(HEIGHT // CELL_SIZE)]

mouse = {'left': False, 'right': False}
clicked_coords = []

print(len(matrix), len(matrix[0]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                mouse['left'] = True
            if event.button == 3: # right click
                mouse['right'] = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # left click
                mouse['left'] = False
            if event.button == 3: # right click
                mouse['right'] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                printMatrix()

    if mouse['left'] or mouse['right']:
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // CELL_SIZE  # mouse_pos[1] = y pos
        col = mouse_pos[0] // CELL_SIZE  # mouse_pos[0] = x pos

        if row < len(matrix) and col < len(matrix[0]):
            if mouse['left']: matrix[row][col] = 1
            elif mouse['right']: matrix[row][col] = 0

    screen.blit(bg_surf, (0, 0))
    draw_grid()
    display_clicked()

    pygame.display.update()
    clock.tick(10000000000000)
