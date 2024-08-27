import pygame
import random
from settings import screen, WHITE

class Ball:
    def __init__(self, color, size, letter, speed):
        self.color = color
        self.size = size
        self.letter = letter
        self.x = random.randint(0, screen.get_width() - size)
        self.y = random.randint(-screen.get_height(), 0)
        self.speed = speed
        # self.speed = random.randint(min_speed, max_speed)  # ランダム速度のコード（コメントアウト）

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
        font = pygame.font.Font(None, 36)
        text = font.render(self.letter, True, WHITE)
        text_rect = text.get_rect(center=(self.x, self.y))
        surface.blit(text, text_rect)

    def update(self):
        self.y += self.speed

    def reset(self):
        self.x = random.randint(0, screen.get_width() - self.size)
        self.y = random.randint(-screen.get_height(), 0)
        # self.speed = random.randint(self.min_speed, self.max_speed)  # ランダム速度のコード（コメントアウト）

    def check_collision(self, other_x, other_y, other_radius):
        distance = ((self.x - other_x) ** 2 + (self.y - other_y) ** 2) ** 0.5
        return distance < (self.size + other_radius)

class Projectile:
    def __init__(self, x, y, size=20):  # デフォルトサイズを20に変更
        self.x = x
        self.y = y
        self.size = size  # サイズを20に設定

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

    def update(self):
        self.y -= 10  # スペースキーでの速度

    def off_screen(self):
        return self.y < 0

