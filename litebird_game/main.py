import pygame
import sys
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, MAIN_MENU_BACKGROUND_IMAGE_PATH

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Menu")

    # Load and scale the background image
    background_image = pygame.image.load(MAIN_MENU_BACKGROUND_IMAGE_PATH)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load and scale the additional image to 1/4 of its original size
    additional_image_path = 'litebird_satellite_2022-0220-2300.png'
    additional_image = pygame.image.load(additional_image_path)
    
    # Get the original size of the image
    original_width, original_height = additional_image.get_size()
    
    # Calculate new size 
    new_width = original_width // 1.3
    new_height = original_height // 1.3
    
    # Scale the image
    additional_image = pygame.transform.scale(additional_image, (new_width, new_height))

    # Calculate position to place the image in the center of the right half of the screen
    image_x = SCREEN_WIDTH // 2 + (SCREEN_WIDTH // 2 - new_width) // 2
    image_y = (SCREEN_HEIGHT - new_height) // 2

    font = pygame.font.Font(None, 74)
    
    # Update text rendering and positioning
    title_text = font.render("GET B-mode GAME!!!", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 120))
    
    score_text = font.render("   [enter] game start ", True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2+100))
    
    view_scores_text = font.render("   [s]   view Scores", True, WHITE)
    view_scores_rect = view_scores_text.get_rect(center=(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 + 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = Game()
                    game.start_game()
                if event.key == pygame.K_s:
                    game = Game()
                    game.show_score()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))  # Draw the main background
        screen.blit(additional_image, (image_x, image_y))  # Draw the additional image in the center of the right half
        screen.blit(title_text, title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(view_scores_text, view_scores_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
