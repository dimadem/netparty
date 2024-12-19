# src/core/game.py
import pygame
from pathlib import Path
from contextlib import contextmanager

# Constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FPS = 30
SCALE_FACTOR = 0.8
SPACESHIP_SCALE = 0.5
ANIMATION_SPEED = 0.3
ANIMATION_BOUNDS = (390, 410)

class Game:
    def __init__(self):
        pygame.init()
        self._init_display()
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        
        # Создаем буфер для двойной буферизации
        self.buffer = pygame.Surface(self.screen.get_size())
        self.buffer = self.buffer.convert_alpha()
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.scenes = {}
        self.current_scene = None
        self.next_scene = None

    def _init_display(self):
        pygame.display.set_caption("Pender Party")
        # Используем аппаратное ускорение и вертикальную синхронизацию
        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWACCEL,
            vsync=1
        )
        # Устанавливаем приоритет таймера для более точного времени
        pygame.time.set_timer(pygame.USEREVENT, 1000 // FPS)

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

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        
    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.next_scene = scene_name

    def handle_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                # Добавляем проброс события в текущую сцену
                if self.current_scene:
                    print(f"Game: пробрасываем событие в сцену {self.current_scene}")  # Отладочный вывод
                    self.scenes[self.current_scene].handle_input(event)

    def update(self, dt):
        # Обработка смены сцены
        if self.next_scene:
            if self.current_scene:
                self.scenes[self.current_scene].on_exit()
            self.current_scene = self.next_scene
            self.scenes[self.current_scene].on_enter()
            self.next_scene = None

        # Обновление текущей сцены
        if self.current_scene:
            self.scenes[self.current_scene].update(dt)

    def draw(self):
        # Очищаем буфер
        self.buffer.fill((0, 0, 0, 0))
        
        # Рисуем текущую сцену в буфер
        if self.current_scene:
            self.scenes[self.current_scene].draw(self.buffer)
        
        # Копируем буфер на экран
        self.screen.blit(self.buffer, (0, 0))
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
