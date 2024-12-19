from app.core.sprite import Sprite
from app.core.animation import PositionAnimation
from app.core.scene import BaseScene

class ViewportScene(BaseScene):
    def __init__(self):
        self.fire_position = [700, 370]
        self.fire_scale = 1 / 4
        self.fire_orange = Sprite('assets/pender_party/viewport/fire_orange.png', self.fire_position, 0, self.fire_scale)
        self.fire_red = Sprite('assets/pender_party/viewport/fire_red.png', self.fire_position, 0, self.fire_scale)
        self.fire_yellow = Sprite('assets/pender_party/viewport/fire_yellow.png', self.fire_position, 0, self.fire_scale)
        self.space_black = Sprite('assets/pender_party/viewport/space_black.png', (800, 0), 0, 0.2)
        self.space_purple = Sprite('assets/pender_party/viewport/space_purple.png', (700, 0), 0, 0.5)
        self.spaceship = Sprite('assets/pender_party/viewport/spaceship.svg', (-60, 600), 0, 0.2)
        self.spaceship_animation = None
        self.fire_sprites = [self.fire_red, self.fire_orange, self.fire_yellow, self.fire_orange]
        self.fire_animations = []
        self.elapsed_time = 0
        
        super().__init__()

    def initialize(self):
        """Initialize viewport scene objects"""
        self._setup_spaceship_animation()
        self._setup_fire_animations()

    def _setup_spaceship_animation(self):
        start_x = -60      # Начальная позиция слева
        end_x = 2400       # Конечная позиция справа
        start_y = 600      # Начальная позиция внизу
        end_y = 100        # Конечная позиция вверху
        
        self.spaceship_animation = PositionAnimation(
            self.spaceship,
            duration=30.0,
            start_pos=(start_x, start_y),
            end_pos=(end_x, end_y),
            loop=True,
            ping_pong=False
        )
        
        # Добавляем небольшой наклон спрайта в сторону движения
        self.spaceship.rotation = -15  # градусов против часовой стрелки

    def _setup_fire_animations(self):
        # Создаем разные анимации для каждого спрайта огня
        animations_params = [
            # dx, dy - смещение от базовой позиции
            {'dx': -15, 'dy': -15, 'duration': 1.8},  # Влево-вверх
            {'dx': 15, 'dy': -20, 'duration': 2.0},   # Вправо-вверх
            {'dx': 0, 'dy': -25, 'duration': 1.5},    # Вертикально
            {'dx': -10, 'dy': -18, 'duration': 1.7},  # По диагонали
        ]

        for sprite, params in zip(self.fire_sprites, animations_params):
            base_x, base_y = self.fire_position
            animation = PositionAnimation(
                sprite,
                duration=params['duration'],
                start_pos=(base_x + params['dx'], base_y),
                end_pos=(base_x, base_y + params['dy']),
                loop=True,
                ping_pong=True,
                phase_shift=params['duration'] * 0.25  # Разные фазы для каждого спрайта
            )
            self.fire_animations.append(animation)

    def handle_input(self, event):
        """Handle input events"""
        pass

    def update(self, dt):
        if not self.active:
            return
        super().update(dt)
        
        self.elapsed_time += dt  # Обновляем счетчик времени
        
        # Обновляем анимацию корабля
        if self.spaceship_animation:
            self.spaceship_animation.update(dt)
        
        # Обновляем анимации огня
        for animation in self.fire_animations:
            animation.update(dt)

    def draw(self, screen):
        # self.space_black.draw(screen)
        self.space_purple.draw(screen)
        self.spaceship.draw(screen)
        # Отрисовываем все спрайты огня
        for sprite in self.fire_sprites:
            sprite.draw(screen)