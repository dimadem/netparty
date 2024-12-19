from app.core.sprite import Sprite
from app.core.scene import BaseScene
from app.core.animation import PositionAnimation
import pygame

class Stickers(BaseScene):
    def __init__(self):
        self.stickers = {}
        self.sticker_animations = {}
        self.sticker_states = {}
        self.base_position = (1920 - 700, 1200)
        self.up_position = (1920 - 700, 600)
        super().__init__()
        self.active = True

    def initialize(self):
        print("Инициализация стикеров...")
        SCALE = 1
        
        # Словарь стикеров и их клавиш
        sticker_configs = {
            'buy_pender': ('buy_pender.svg', pygame.K_z),
            'crossed_hands': ('crossed_hands.svg', pygame.K_x),
            'dump': ('dump.svg', pygame.K_c),
            'kiss_my_ass': ('kiss_my_ass.svg', pygame.K_v),
            'kissed': ('kissed.svg', pygame.K_b),
            'peace': ('peace.svg', pygame.K_n),
            'sleep_on_cash': ('sleep_on_cash.svg', pygame.K_m),
            'up_up_up': ('up_up_up.svg', pygame.K_COMMA)
        }

        # Создаем все стикеры
        for name, (file, key) in sticker_configs.items():
            sprite = self.add_sprite(name, 
                Sprite(f'assets/pender_party/stickers/{file}', 
                      self.base_position, 0, SCALE))
            self.stickers[key] = sprite
            self.sticker_states[key] = False
            self._create_animation(key, going_up=False)
            self.sticker_animations[key].stop()

    def _create_animation(self, key, going_up):
        start_pos = self.base_position if going_up else self.up_position
        end_pos = self.up_position if going_up else self.base_position
        
        self.sticker_animations[key] = PositionAnimation(
            sprite=self.stickers[key],
            duration=0.5,
            start_pos=start_pos,
            end_pos=end_pos,
            loop=False,
            ping_pong=False
        )

    def handle_input(self, event):
        if not self.active:
            return
            
        if event.type == pygame.KEYDOWN:
            if event.key in self.stickers:
                print(f"Переключение стикера: {'вверх' if not self.sticker_states[event.key] else 'вниз'}")
                self.sticker_states[event.key] = not self.sticker_states[event.key]
                self._create_animation(event.key, going_up=self.sticker_states[event.key])
                self.sticker_animations[event.key].reset()
                self.sticker_animations[event.key].start()

    def update(self, dt):
        if not self.active:
            return
        
        for animation in self.sticker_animations.values():
            if animation:
                animation.update(dt)

    def draw(self, screen):
        for sticker in self.stickers.values():
            sticker.draw(screen)
