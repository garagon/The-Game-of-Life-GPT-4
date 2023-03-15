import pygame
import numpy as np
import time

# Configuración inicial
width, height = 800, 800
nX, nY = 80, 80
xSize, ySize = width // nX, height // nY

# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
bg = 25, 25, 25
screen.fill(bg)

# Estado inicial aleatorio de las celdas
state = np.random.randint(0, 2, (nX, nY))

# Función para dibujar las celdas
def draw(state):
    for y in range(0, nY):
        for x in range(0, nX):
            if state[x, y]:
                pygame.draw.rect(screen, (255, 255, 255), (x * xSize, y * ySize, xSize, ySize))
            else:
                pygame.draw.rect(screen, bg, (x * xSize, y * ySize, xSize, ySize))
            pygame.draw.line(screen, (50, 50, 50), (x * xSize, 0), (x * xSize, height), 1)
            pygame.draw.line(screen, (50, 50, 50), (0, y * ySize), (width, y * ySize), 1)

# Función para dibujar el botón de pausa
def draw_pause_button(paused):
    pause_color = (0, 255, 0) if paused else (255, 0, 0)
    pygame.draw.rect(screen, pause_color, (width - 220, 10, 100, 40))
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Pause" if not paused else "Resume", True, (255, 255, 255))
    screen.blit(pause_text, (width - 210, 15))

# Función para dibujar el botón de salida
def draw_exit_button():
    exit_color = (255, 0, 0)
    pygame.draw.rect(screen, exit_color, (width - 110, 10, 100, 40))
    font = pygame.font.Font(None, 36)
    exit_text = font.render("Exit", True, (255, 255, 255))
    screen.blit(exit_text, (width - 100, 15))

# Función para dibujar el título
def draw_title():
    font = pygame.font.Font(None, 48)
    title_text = font.render("The Game of Life", True, (200, 200, 200))
    screen.blit(title_text, (10, 10))

# Bucle principal
running = True
paused = False
while running:

    # Eventos de entrada
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 10 <= y <= 50 and width - 220 <= x <= width - 120:
                paused = not paused
            elif 10 <= y <= 50 and width - 110 <= x <= width - 10:
                running = False

    if not paused:
        new_state = np.copy(state)
        for y in range(0, nY):
            for x in range(0, nX):
                n_neighbors = np.sum(state[(x-1)%nX:(x+2)%nX, (y-1)%nY:(y+2)%nY]) - state[x, y]
                if state[x, y] and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif not state[x, y] and n_neighbors == 3:
                    new_state[x, y] = 1
        state = new_state

    screen.fill(bg)
    draw(state)
    draw_pause_button(paused)
    draw_exit_button()
    draw_title()
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()