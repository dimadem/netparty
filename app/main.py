from app.core.game import Game, game_context
from app.scenes.viewport import ViewportScene
from app.scenes.club import ClubScene
from app.scenes.room import RoomScene
import pygame

class PenderParty(Game):
    def __init__(self):
        super().__init__()
        self.scenes = {
            'room': RoomScene(),
            'viewport': ViewportScene(),
            'club': ClubScene(),
        }
        self.current_scene = 'room'

    def update(self, dt):
        self.scenes['viewport'].update(dt)
        self.scenes['room'].update(dt)
        self.scenes['club'].update(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Отрисовываем сцены в нужном порядке наслоения
        self.scenes['viewport'].draw(self.screen)  # Сначала viewport (нижний слой)
        self.scenes['room'].draw(self.screen)      # Затем room (средний слой)
        self.scenes['club'].draw(self.screen)      # И наконец club (верхний слой)
        pygame.display.flip()  # Добавляем обновление экрана

def main():
    with game_context():
        pender_party = PenderParty()
        pender_party.run()

if __name__ == "__main__":
    main()
