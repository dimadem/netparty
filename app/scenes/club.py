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
            Sprite('assets/pender_party/club/discoball.png', (1920 - (1920 / 2.9), -90), 0, 0.7))
        # Инициализация конфигурации прожекторов
        self.spot_configs = [
            {'pos': [0, -100], 'angle': 0, 'scale': 1.0, 'speed': 2.0},
            {'pos': [1400, -100], 'angle': 90, 'scale': 1.0, 'speed': 1.5},
            {'pos': [600, -100], 'angle': 45, 'scale': 0.8, 'speed': 1.7}
        ]

        self.spot_animations = []
        self._create_spotlights()
        self._setup_spotlight_animations()

    def _create_spotlights(self):
        """Create spotlight sprites"""
        self.spot_sprites = []
        for i, config in enumerate(self.spot_configs):
            spot_group = []
            for j in range(1, 5):
                sprite = self.add_sprite(f'spot_{i}_{j}',
                    Sprite(f'assets/pender_party/club/spot_{j}.png',
                          config['pos'],
                          config['angle'],
                          config['scale']))
                spot_group.append(sprite)
            self.spot_sprites.append(spot_group)

    def _setup_spotlight_animations(self):
        """Setup animations for spotlights"""
        for i, config in enumerate(self.spot_configs):
            for j, sprite in enumerate(self.spot_sprites[i], 1):
                anim = AlphaAnimation(
                    sprite=sprite,
                    duration=config['speed'],
                    loop=True,
                    phase_shift=j * math.pi / 2,
                    start_alpha=0,
                    end_alpha=255
                )
                self.spot_animations.append(anim)

    def update(self, dt):
        if not self.active:
            return
        # update lights
        for lights in self.spot_animations:
            lights.update(dt)
        
        super().update(dt)

    def draw(self, screen):
        # discoball
        self.discoball.draw(screen)
        # lights
        for _, lights in self.sprites.items():
            lights.draw(screen)

    def handle_input(self, event):
        """Handle input events"""
        pass  # Добавляем обязательную реализацию абстрактного метода