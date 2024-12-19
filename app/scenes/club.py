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
        
        self.colors = ['blue', 'lightrose', 'purple', 'rose']
        self.spot_animations = []
        self._create_spotlights()
        self._setup_spotlight_animations()

    def _create_spotlights(self):
        """Create spotlight sprites"""
        self.spot_sprites = []
        base_config = {'pos': [0, 0], 'angle': 0, 'scale': 0.25}
        
        spot_group = []
        for ray_num in range(3, 6):  # 7 групп лучей
            color_group = []
            for color in self.colors:
                sprite = self.add_sprite(
                    f'spot_{ray_num}_{color}',
                    Sprite(f'assets/pender_party/club/{ray_num}{color}.png',
                          base_config['pos'],
                          base_config['angle'],
                          base_config['scale'])
                )
                color_group.append(sprite)
            spot_group.append(color_group)
        self.spot_sprites.append(spot_group)

    def _setup_spotlight_animations(self):
        """Setup animations for spotlights"""
        for ray_num, ray_group in enumerate(self.spot_sprites[0], 1):
            # Добавляем противофазу: нечетные (1,3,5,7) vs четные (2,4,6) группы
            opposite_phase = math.pi if ray_num % 2 == 0 else 0
            
            for j, sprite in enumerate(ray_group):
                anim = AlphaAnimation(
                    sprite=sprite,
                    duration=2.0,
                    loop=True,
                    phase_shift=(ray_num * math.pi / 7) + (j * math.pi / 4) + opposite_phase,
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