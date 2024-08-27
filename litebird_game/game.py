import pygame
import os
import sys
import random
import time
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, RED, BLUE, SCORE_FILE, font, GAME_BACKGROUND_IMAGE_PATH, SPECIAL_IMAGE_PATH, SPECIAL_IMAGE_SPEED, SPECIAL_IMAGE_INTERVAL
from player import Player
from ball import Ball, Projectile

class Game:
    def __init__(self):
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        self.player = Player()

        # EとBmodeの速度，数
        self.red_ball_speed = 7  # E速度
        self.blue_ball_speed = 8  # Bの速度

        self.num_red_balls = 12  # Eの数
        self.num_blue_balls = 3  # Bの数

        self.red_balls = [Ball(RED, 30, "E", self.red_ball_speed) for _ in range(self.num_red_balls)]
        self.blue_balls = [Ball(BLUE, 30, "B", self.blue_ball_speed) for _ in range(self.num_blue_balls)]
        self.projectiles = []
        self.special_images = []  # ギミック画像を管理するリスト
        self.special_image_timer = time.time()  # ギミック画像のタイマーを初期化

        self.clock = pygame.time.Clock()
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()
        
        # gameの時間
        game_duration = 30
        self.game_duration = game_duration * 1000
        self.game_background = self.load_background_image(GAME_BACKGROUND_IMAGE_PATH)

    def load_background_image(self, image_path):
        try:
            image = pygame.image.load(image_path)
            return pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except pygame.error as e:
            print(f"Unable to load image {image_path}. Error: {e}")
            return None

    def load_special_image(self):
        try:
            image = pygame.image.load(SPECIAL_IMAGE_PATH)
            image = pygame.transform.scale(image, (80, 80))  # サイズを80x80に変更
            return image
        except pygame.error as e:
            print(f"Unable to load image {SPECIAL_IMAGE_PATH}. Error: {e}")
            return None


    def save_score(self):
        with open(SCORE_FILE, "a") as f:
            f.write(f"{self.score}\n")

    def load_scores(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                scores = [int(line.strip()) for line in f]
            return sorted(scores, reverse=True)
        return []

    def draw_text(self, text, pos, color=WHITE):
        screen.blit(font.render(text, True, color), pos)

# コントローラーで動かそうとしてるけど，今のところ反応しない　ヌルポ!?
    def update_player_with_controller(self):
        if self.joystick:
            x_axis = self.joystick.get_axis(0)
            if x_axis < -0.5:
                self.player.update("left")
            elif x_axis > 0.5:
                self.player.update("right")

            button_enter = 2
            button_s = 0

            if self.joystick.get_button(button_enter):
                self.start_game()
            if self.joystick.get_button(button_s):
                self.show_score()

    def start_game(self):
        self.run()

    def run(self):
        running = True
        while running:
            if self.game_background:
                screen.blit(self.game_background, (0, 0))
            else:
                screen.fill(WHITE)

            elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000
            remaining_time = max(0, int(self.game_duration / 1000 - elapsed_time))
            self.draw_text(f"Time: {remaining_time}", (10, 10))
            self.draw_text(f"Score: {self.score}", (10, 60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # シューティング要素
                        self.projectiles.append(Projectile(self.player.x + self.player.width // 2, self.player.y, 12))

            self.update_player_with_controller()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.update("left")
            if keys[pygame.K_RIGHT]:
                self.player.update("right")

            self.player.draw(screen)

            # 描画の更新
            for projectile in self.projectiles[:]:
                projectile.update()
                projectile.draw(screen)
                if projectile.off_screen():
                    self.projectiles.remove(projectile)

            # Update 赤玉(Emode)
            for red_ball in self.red_balls[:]:
                red_ball.update()
                red_ball.draw(screen)
                if self.player.catch(red_ball):
                    self.score = max(0, self.score + 1)  # 赤い球は+1点スコアは0以下にはならない
                    red_ball.reset()
                if red_ball.y > SCREEN_HEIGHT:
                    red_ball.reset()

            # Update 青玉(Emode)
            for blue_ball in self.blue_balls:
                blue_ball.update()
                blue_ball.draw(screen)
                if self.player.catch(blue_ball):
                    self.score = max(0, self.score + 10)  # 青い球は+10スコアは0以下にはならない
                    blue_ball.reset()
                if blue_ball.y > SCREEN_HEIGHT:
                    blue_ball.reset()

            # 地球あてギミック
            for projectile in self.projectiles[:]:
                for img in self.special_images[:]:
                    img_rect = pygame.Rect(img['x'], img['y'], 80, 80)
                    if img_rect.colliderect(projectile.x - projectile.size // 2, projectile.y - projectile.size // 2, projectile.size, projectile.size):
                        self.special_images.remove(img)
                        self.projectiles.remove(projectile)
                        self.score *= 2  # スコアを2倍にする
                        break

            # ギミック画像のタイマー処理
            if time.time() - self.special_image_timer >= SPECIAL_IMAGE_INTERVAL:
                special_image = self.load_special_image()
                if special_image:
                    self.special_images.append({'image': special_image, 'x': random.randint(0, SCREEN_WIDTH - 50), 'y': -50})
                self.special_image_timer = time.time()

            # ギミック画像の位置更新
            for img in self.special_images:
                img['y'] += SPECIAL_IMAGE_SPEED
            
            # 画面外に出た画像を削除
            self.special_images = [img for img in self.special_images if img['y'] < SCREEN_HEIGHT]

            # ギミック画像を描画
            for img in self.special_images:
                screen.blit(img['image'], (img['x'], img['y']))

            pygame.display.flip()
            self.clock.tick(60)

            if elapsed_time >= (self.game_duration / 1000):
                running = False

            #地球にあてたときにエフェクトを出したいなって思ってるができない


        self.save_score()
        self.show_score()

    def show_score(self):
        screen.fill(WHITE)
        self.draw_text(f"Final Score: {self.score}", (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150), BLACK)
        self.draw_text("Press ENTER to Return to Menu", (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 50), BLACK)

        scores = self.load_scores()
        y_offset = SCREEN_HEIGHT // 2 + 50
        for i, score in enumerate(scores[:10]):
            self.draw_text(f"{i + 1}. {score}", (SCREEN_WIDTH // 2 - 100, y_offset), BLACK)
            y_offset += 50

        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        return
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 2:
                        waiting = False
                        return

if __name__ == "__main__":
    print("main script is main.py")
    print("please do main.py")
