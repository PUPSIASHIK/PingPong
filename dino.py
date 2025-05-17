import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Создание объектов
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
paddle1 = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)

ball_speed_x = 7
ball_speed_y = 7

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение ракеток
    keys = pygame.key.get_pressed()
    
    # Управление первого игрока (W/S)
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 10
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 10

    # Управление второго игрока (стрелки)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 10
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 10

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Удар о стенки
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Удар о ракетки
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    # Переход мяча за пределы
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2  # Восстановление позиции мяча

    # Очистка экрана
    screen.fill(BLACK)
    # Рисование объектов
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(30)