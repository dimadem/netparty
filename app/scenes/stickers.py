from app.core.sprite import Sprite
from app.core.scene import BaseScene
from app.core.animation import PositionAnimation
import pygame

class Stickers(BaseScene):
    def __init__(self):
        super().__init__()
        self.active = True  # Явно активируем сцену
        
        self.base_path = 'assets/pender_party/stickes/'
        self.default_scale = 1.0
        self.default_rotation = 0
        
        # Позиции стикеров
        self.buy_pender_pos = [100, 100]
        self.crossed_hands_pos = [200, 100]
        self.dump_pos = [300, 100]
        self.happy_cash_pos = [400, 100]
        self.kiss_ass_pos = [500, 100]
        self.kissed_pos = [100, 200]
        self.peace_pos = [200, 200]
        self.sleep_cash_pos = [300, 200]
        self.up_up_pos = [400, 200]

        # Создание спрайтов стикеров
        self.buy_pender = Sprite(f"{self.base_path}buy_pender.svg", self.buy_pender_pos, self.default_rotation, self.default_scale)
        self.crossed_hands = Sprite(f"{self.base_path}crossed_hands.svg", self.crossed_hands_pos, self.default_rotation, self.default_scale)
        self.dump = Sprite(f"{self.base_path}dump.svg", self.dump_pos, self.default_rotation, self.default_scale)
        self.happy_in_cash = Sprite(f"{self.base_path}happy_in_cash.svg", self.happy_cash_pos, self.default_rotation, self.default_scale)
        self.kiss_my_ass = Sprite(f"{self.base_path}kiss_my_ass.svg", self.kiss_ass_pos, self.default_rotation, self.default_scale)
        self.kissed = Sprite(f"{self.base_path}kissed.svg", self.kissed_pos, self.default_rotation, self.default_scale)
        self.peace = Sprite(f"{self.base_path}peace.svg", self.peace_pos, self.default_rotation, self.default_scale)
        self.sleep_on_cash = Sprite(f"{self.base_path}sleep_on_cash.svg", self.sleep_cash_pos, self.default_rotation, self.default_scale)
        self.up_up_up = Sprite(f"{self.base_path}up_up_up.svg", self.up_up_pos, self.default_rotation, self.default_scale)

        # Список всех стикеров
        self.all_stickers = [
            self.buy_pender,
            self.crossed_hands,
            self.dump,
            self.happy_in_cash,
            self.kiss_my_ass,
            self.kissed,
            self.peace,
            self.sleep_on_cash,
            self.up_up_up
        ]

        # Анимации для каждого стикера
        self.buy_pender_animation = self._create_animation(self.buy_pender, self.buy_pender_pos)
        self.crossed_hands_animation = self._create_animation(self.crossed_hands, self.crossed_hands_pos)
        self.dump_animation = self._create_animation(self.dump, self.dump_pos)
        self.happy_cash_animation = self._create_animation(self.happy_in_cash, self.happy_cash_pos)
        self.kiss_ass_animation = self._create_animation(self.kiss_my_ass, self.kiss_ass_pos)
        self.kissed_animation = self._create_animation(self.kissed, self.kissed_pos)
        self.peace_animation = self._create_animation(self.peace, self.peace_pos)
        self.sleep_cash_animation = self._create_animation(self.sleep_on_cash, self.sleep_cash_pos)
        self.up_up_animation = self._create_animation(self.up_up_up, self.up_up_pos)

        # Список всех анимаций
        self.all_animations = [
            self.buy_pender_animation,
            self.crossed_hands_animation,
            self.dump_animation,
            self.happy_cash_animation,
            self.kiss_ass_animation,
            self.kissed_animation,
            self.peace_animation,
            self.sleep_cash_animation,
            self.up_up_animation
        ]

        # Словарь для маппинга клавиш к стикерам
        self.key_mapping = {
            pygame.K_z: (self.buy_pender, self.buy_pender_animation),
            pygame.K_x: (self.crossed_hands, self.crossed_hands_animation),
            pygame.K_c: (self.dump, self.dump_animation),
            pygame.K_v: (self.happy_in_cash, self.happy_cash_animation),
            pygame.K_b: (self.kiss_my_ass, self.kiss_ass_animation),
            pygame.K_n: (self.kissed, self.kissed_animation),
            pygame.K_m: (self.peace, self.peace_animation),
            pygame.K_COMMA: (self.sleep_on_cash, self.sleep_cash_animation),
            pygame.K_PERIOD: (self.up_up_up, self.up_up_animation)
        }

    def _create_animation(self, sprite, start_pos):
        """Вспомогательный метод для создания анимации стикера"""
        animation = PositionAnimation(
            sprite,
            duration=0.5,  # Уменьшаем длительность
            start_pos=start_pos,
            end_pos=(start_pos[0], start_pos[1] - 100),  # Увеличиваем амплитуду движения
            loop=False,
            ping_pong=True
        )
        animation.target = sprite  # Добавляем явное указание цели анимации
        animation.start_position = start_pos  # Сохраняем начальную позицию
        return animation

    def handle_input(self, event):
        """Обработка нажатий клавиш"""
        if event.type == pygame.KEYDOWN and event.key in self.key_mapping:
            sticker, animation = self.key_mapping[event.key]
            # Сбрасываем позицию стикера на начальную
            sticker.position = animation.start_position
            # Запускаем анимацию
            animation.start()

    def update(self, dt):
        if not self.active:
            return
        super().update(dt)
        
        # Обновляем все активные анимации
        for animation in self.all_animations:
            if animation.is_running:
                animation.update(dt)
                
    def draw(self, screen):
        if not self.active:
            return
        # Отрисовываем все стикеры
        for sticker in self.all_stickers:
            sticker.draw(screen)

    def initialize(self):
        """Initialize stickers scene"""
        pass
