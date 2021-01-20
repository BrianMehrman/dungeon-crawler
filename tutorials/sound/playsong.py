import pygame
from utils import local_file

class Print():
    def __init__(self):
        self.font = pygame.font.Font(None, 32)

    def draw(self, surface, msg, position):
        obj = self.font.render(msg, True, (255, 255, 255))

        surface.blit(obj, position)

    
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    fps_clock = pygame.time.Clock()
    surface = pygame.display.set_mode((640, 480))
    out = Print()
    out = Print()
    out = Print()

    song = pygame.mixer.Sound(local_file('bensound-theelevatorbossanova.ogg'))
    song.play(-1)

    running = True
    paused = False
    fading = False
    volume = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1000)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    if paused:
                        pygame.mixer.pause()
                    else:
                        pygame.mixer.unpause()
                elif event.key == pygame.K_ESCAPE and not fading:
                    fading = True
                    pygame.mixer.fadeout(1000)
                elif event.key == pygame.K_LEFTBRACKET:
                    volume -= 0.1
                    if volume < 0:
                        volume = 0
                    song.set_volume(volume)

                elif event.key == pygame.K_RIGHTBRACKET:
                    volume += 0.1
                    if volume > 1:
                        volume = 1
                    song.set_volume(volume)
        
        if not pygame.mixer.get_busy():
            running = False

        surface.fill((0,0,0))

        out.draw(surface, "Press <SPACE> to pause / unpause the music", (4,4))
        out.draw(surface, "Press <ESC> to fade out and close program", (4,36))
        out.draw(surface, "Press [ and ] to alter the volume", (4,68))
        out.draw(surface, "Current volume: {0:1.2f}".format(volume), (4, 100))

        pygame.display.update()
        fps_clock.tick(30)

    pygame.mixer.quit()
    pygame.quit()