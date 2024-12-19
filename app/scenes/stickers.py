from app.core.sprite import Sprite
from app.core.scene import BaseScene
from app.core.animation import PositionAnimation
import pygame

class Stickers(BaseScene):
    def __init__(self):
        self.sticker_animation = None
        self.is_up = False  # Флаг положения стикера
        self.base_position = (1920 - 700, 1200)  # Позиция внизу (за пределами экрана)
        self.up_position = (1920 - 700, 600)     # Позиция вверху (видимая)
        super().__init__()
        self.active = True

    def initialize(self):
        print("Инициализация buy_pender стикера...")
        SCALE = 1
        
        # Создаем стикер в начальной позиции (за пределами экрана)
        self.buy_pender = self.add_sprite('buy_pender', 
            Sprite('assets/pender_party/stickers/buy_pender.svg', self.base_position, 0, SCALE))
        
        # Создаем начальную анимацию, но не запускаем её
        self._create_animation(going_up=True)
        self.sticker_animation.stop()  # Останавливаем анимацию сразу

    def _create_animation(self, going_up):
        # Создаем анимацию в зависимости от направления
        start_pos = self.base_position if going_up else self.up_position
        end_pos = self.up_position if going_up else self.base_position
        
        self.sticker_animation = PositionAnimation(
            sprite=self.buy_pender,
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
            if event.key == pygame.K_z:
                print(f"Переключение стикера: {'вверх' if not self.is_up else 'вниз'}")
                self.is_up = not self.is_up  # Переключаем состояние
                self._create_animation(going_up=self.is_up)  # Создаем анимацию в нужном направлении
                self.sticker_animation.reset()
                self.sticker_animation.start()

    def update(self, dt):
        if not self.active:
            return
        
        if self.sticker_animation:
            self.sticker_animation.update(dt)

    def draw(self, screen):
        self.buy_pender.draw(screen)
