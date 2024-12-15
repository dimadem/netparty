from app.core.sprite import Sprite
import math

class ViewportScene:
    def __init__(self):
        self.fire_orange = Sprite('assets/pender_party/viewport/fire_orange.png', (0, 0), 1.0)
        self.fire_red = Sprite('assets/pender_party/viewport/fire_red.png', (0, 0), 1.0)
        self.fire_yellow = Sprite('assets/pender_party/viewport/fire_yellow.png', (0, 0), 1.0)
        self.space_black = Sprite('assets/pender_party/viewport/space_black.png', (1200, 0), 0.2)
        self.space_purple = Sprite('assets/pender_party/viewport/space_purple.png', (0, 0), 0.5)
        self.spaceship = Sprite('assets/pender_party/viewport/spaceship.svg', (1200, 300), 0.5)
        self.fire_sprites = [self.fire_orange, self.fire_red, self.fire_yellow]
        self.animation_time = 0
        self.current_fire = 0

    def _fire_animation(self, dt):
        self.animation_time += dt
        
        # Меняем текущий спрайт огня каждые 0.2 секунды
        if self.animation_time >= 0.2:
            self.current_fire = (self.current_fire + 1) % len(self.fire_sprites)
            self.animation_time = 0
            
        # Добавляем колебательное движение
        offset_y = math.sin(self.animation_time * 10) * 5
        current_sprite = self.fire_sprites[self.current_fire]
        current_sprite.position = (current_sprite.position[0], offset_y)


    def update(self, dt):
        self._fire_animation(dt)

    def draw(self, screen):
        self.space_black.draw(screen)
        # self.space_purple.draw(screen)
        # self.fire_sprites[self.current_fire].draw(screen)
        self.spaceship.draw(screen)