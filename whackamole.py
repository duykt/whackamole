import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_pos = (0,0)
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ((event.pos[0] // 32) == (mole_pos[0] // 32)) and ((event.pos[1] // 32) == (mole_pos[1] // 32)):
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)
                        mole_pos = (x * 32, y * 32)

            screen.fill("light green")
            # vertical lines
            for i in range(20):
                pygame.draw.line(screen, "dark green", (i * 32, 0), (i * 32, 512))

            # horizontal line
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, i * 32), (640, i * 32))

            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
