from app.core.sprite import Sprite
from app.core.scene import BaseScene
from app.core.animation import AlphaAnimation
import math

class ClubScene(BaseScene):
    def __init__(self):
        super().__init__()  # Добавляем вызов родительского конструктора

    def initialize(self):
        """Initialize club scene objects"""
        # Инициализация спрайтов
        self.discoball = self.add_sprite('discoball', 
            Sprite('assets/pender_party/club/discoball.png', (1920 - 1920 / 2.8, -120), 0, 1.0))

        # Инициализация прожекторов
        self.spot_configs = [
            {'pos': [0, -100], 'angle': 0, 'scale': 1.0, 'speed': 2.0},
            {'pos': [1400, -100], 'angle': 90, 'scale': 1.0, 'speed': 1.5},
            {'pos': [600, -100], 'angle': 45, 'scale': 0.8, 'speed': 1.7}
        ]

        self.spot_animations = []
        
        # Создаем спрайты и анимации для каждого прожектора
        for i, config in enumerate(self.spot_configs):
            spots = []
            for j in range(1, 5):  # 4 луча для каждого прожектора
                sprite = self.add_sprite(f'spot_{i}_{j}',
                    Sprite(f'assets/pender_party/club/spot_{j}.png',
                          config['pos'],
                          config['angle'],
                          config['scale']))
                
                # Создаем анимацию для каждого луча
                anim = AlphaAnimation(
                    sprite=sprite,
                    duration=config['speed'],
                    loop=True,
                    phase_shift=j * math.pi / 2,  # Сдвиг фазы для каждого луча
                    start_alpha=0,
                    end_alpha=255
                )
                self.spot_animations.append(anim)

        # Создаем анимацию для диско-шара
        self.disco_animation = AlphaAnimation(
            sprite=self.discoball,
            duration=1.0,
            loop=True,
            start_alpha=100,
            end_alpha=255
        )

    def update(self, dt):
        if not self.active:
            return
        
        # Обновляем все анимации
        self.disco_animation.update(dt)
        for anim in self.spot_animations:
            anim.update(dt)
        
        super().update(dt)

    def draw(self, screen):
        # Отрисовка всех спрайтов
        for name, sprite in self.sprites.items():
            sprite.draw(screen)

    def handle_input(self, event):
        """Handle input events"""
        pass  # Добавляем обязательную реализацию абстрактного метода