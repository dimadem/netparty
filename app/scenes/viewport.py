from app.core.sprite import Sprite
import math
from app.core.scene import BaseScene

class ViewportScene(BaseScene):
    def __init__(self):
        super().__init__()  # Добавляем вызов родительского конструктора
        self.fire_position = [700, 370]
        self.fire_scale = 1 / 4
        self.fire_orange = Sprite('assets/pender_party/viewport/fire_orange.png', self.fire_position, 0, self.fire_scale)
        self.fire_red = Sprite('assets/pender_party/viewport/fire_red.png', self.fire_position, 0, self.fire_scale)
        self.fire_yellow = Sprite('assets/pender_party/viewport/fire_yellow.png', self.fire_position, 0, self.fire_scale)
        self.space_black = Sprite('assets/pender_party/viewport/space_black.png', (800, 0), 0, 0.2)
        self.space_purple = Sprite('assets/pender_party/viewport/space_purple.png', (700, 0), 0, 0.5)
        self.spaceship = Sprite('assets/pender_party/viewport/spaceship.svg', (1200, 300), 0, 0.5)
        self.fire_sprites = [self.fire_red, self.fire_orange, self.fire_yellow, self.fire_orange]
        self.animation_time = 0
        self.current_fire = 0

    def initialize(self):
        """Initialize viewport scene objects"""
        pass

    def handle_input(self, event):
        """Handle input events"""
        pass

    def _fire_animation(self, dt):
        self.animation_time += dt
        if self.animation_time >= 0.9:
            self.current_fire = (self.current_fire + 1) % len(self.fire_sprites)
            self.animation_time = 0
            
        # Используем базовую позицию + смещение
        offset_y = math.sin(self.animation_time * 10) * 5
        offset_x = math.cos(self.animation_time * 10) * 3
        current_sprite = self.fire_sprites[self.current_fire]
        current_sprite.position = (self.fire_position[0] + offset_x, self.fire_position[1] + offset_y)


    def update(self, dt):
        if not self.active:
            return
        super().update(dt)
        self._fire_animation(dt)

    def draw(self, screen):
        # self.space_black.draw(screen)
        self.space_purple.draw(screen)
        self.spaceship.draw(screen)
        # self.fire_sprites[self.current_fire].draw(screen)