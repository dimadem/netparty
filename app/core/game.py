# src/core/game.py
import pygame
from pathlib import Path
from contextlib import contextmanager

# Constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FPS = 60
SCALE_FACTOR = 0.8
SPACESHIP_SCALE = 0.5
ANIMATION_SPEED = 0.3
ANIMATION_BOUNDS = (390, 410)

class Game:
    def __init__(self):
        pygame.init()
        self._init_display()
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def _init_display(self):
        pygame.display.set_caption("Pender Party")
        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED,
            vsync=1
        )

    def _load_and_scale_image(self, path, scale_factor=None, scale_to_screen=False):
        image = pygame.image.load(path).convert_alpha()
        if scale_to_screen:
            width, height = image.get_size()
            scale = min(WINDOW_WIDTH / width, WINDOW_HEIGHT / height)
            new_size = (int(width * scale), int(height * scale))
        elif scale_factor:
            width, height = image.get_size()
            new_size = (int(width * scale_factor), int(height * scale_factor))
        else:
            return image
        return pygame.transform.scale(image, new_size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.dt = self.clock.tick(FPS) / 1000.0
            self.update(self.dt)
            self.draw()

    def quit(self):
        pygame.quit()

@contextmanager
def game_context():
    game = None
    try:
        game = Game()
        yield game
    finally:
        if game:
            game.quit()
