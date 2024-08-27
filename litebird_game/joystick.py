import pygame

def print_joystick_buttons():
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Joystick detected: ", joystick.get_name())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            if event.type == pygame.QUIT:
                pygame.quit()
                return

print_joystick_buttons()
