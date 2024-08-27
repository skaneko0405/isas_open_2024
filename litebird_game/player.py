import pygame
from settings import screen, WHITE

class Player:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = screen.get_width() // 2 - self.width // 2
        self.y = screen.get_height() - self.height - 10
        self.color = WHITE
        self.speed = 7

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

        # Boundary checking
        if self.x < 0:
            self.x = 0
        if self.x > screen.get_width() - self.width:
            self.x = screen.get_width() - self.width

    def catch(self, ball):
        # Check if the center of the ball is within the player's rectangle
        ball_radius = ball.size
        ball_center_x = ball.x
        ball_center_y = ball.y
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Check if the distance from the ball's center to the closest point on the rectangle is less than the ball's radius
        closest_x = max(self.x, min(ball_center_x, self.x + self.width))
        closest_y = max(self.y, min(ball_center_y, self.y + self.height))
        distance_x = ball_center_x - closest_x
        distance_y = ball_center_y - closest_y
        distance_squared = distance_x ** 2 + distance_y ** 2
        
        return distance_squared < ball_radius ** 2
    
if __name__ == "__main__":
    print("main script is main.py")
    print("please do main.py")
