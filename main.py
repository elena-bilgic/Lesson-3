import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("image/arrows-2889040_640.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/klipartz.com.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Дополнительно были добавлены переменные `flash_duration` и `last_hit_time` для управления вспышкой.
#После попадания в цель (`MOUSEBUTTONDOWN` и проверка координат) обновляем `last_hit_time`.
#Если с момента последнего попадания прошло меньше времени, чем `flash_duration`, заполняем экран белым цветом, чтобы создать эффект вспышки.
#Теперь, когда игрок попадает в цель, будет отображаться короткая белая вспышка.

flash_duration = 100
last_hit_time = 0

running = True
while running:
    current_time = pygame.time.get_ticks()
    screen.fill(color)

    if current_time - last_hit_time < flash_duration:
        #отображение вспышки на экране
        screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                last_hit_time = current_time  # Запоминаем время попадания

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()


