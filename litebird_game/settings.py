import pygame

# Pygameの初期化
pygame.init()

# 画面サイズの設定
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("キャッチゲーム")

# 色の設定
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フォントの設定
font = pygame.font.Font(None, 60)  

# スコア保存ファイル
SCORE_FILE = "scores.txt"

# 背景画像のパス（デフォルト値）
MAIN_MENU_BACKGROUND_IMAGE_PATH = "cos.png"
GAME_BACKGROUND_IMAGE_PATH = "black_00080.jpg"  
# GAME_BACKGROUND_IMAGE_PATH = "cos.png"  

SPECIAL_IMAGE_PATH = 'earth01.png'

# ギミック画像の速度
SPECIAL_IMAGE_SPEED = 5

# ギミック画像が降ってくる間隔（秒）
SPECIAL_IMAGE_INTERVAL = 10



