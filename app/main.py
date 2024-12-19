from app.core.game import Game, game_context
from app.core.composite_scene import CompositeScene
from app.scenes.viewport import ViewportScene
from app.scenes.club import ClubScene
from app.scenes.room import RoomScene
from app.scenes.stickers import Stickers
import pygame

class PenderParty(Game):
    def __init__(self):
        super().__init__()
        self.current_scene = None

    def update(self, dt):
        if self.current_scene:
            self.scenes[self.current_scene].update(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.current_scene:
            self.scenes[self.current_scene].draw(self.screen)
        pygame.display.flip()

def main():
    with game_context() as game:
        # Создаем композитную сцену для главного экрана
        main_scene = CompositeScene()
        
        # Создаем слои
        room_layer = RoomScene()
        club_layer = ClubScene()
        viewport_layer = ViewportScene()
        stickers_layer = Stickers()
        
        # Добавляем слои в правильном порядке отрисовки (от заднего к переднему)
        main_scene.add_layer('viewport', viewport_layer, 0)  # Передний слой
        main_scene.add_layer('room', room_layer, 1)      # Задний фон
        main_scene.add_layer('club', club_layer, 2)      # Средний слой
        main_scene.add_layer('stickers', stickers_layer, 3)
        
        # Добавляем композитную сцену в игру
        game.add_scene('main', main_scene)
        game.change_scene('main')
        
        game.run()

if __name__ == "__main__":
    main()
