from app.core.scene import BaseScene
from app.core.sprite import Sprite

class RoomScene(BaseScene):
    def initialize(self):
        """Initialize scene specific objects"""
        self.add_sprite('background', Sprite('assets/pender_party/room/background_stage.png', (0, 0), 1/4))

    def update(self, dt):
        super().update(dt)
        if not self.active:
            return

    def draw(self, screen):
        self.get_sprite('background').draw(screen)

    def handle_input(self, event):
        """Handle input events"""
        pass
